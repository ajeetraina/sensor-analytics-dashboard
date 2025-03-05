from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = None
        self._connect()

    def _connect(self):
        try:
            self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))
            # Verify connectivity
            self.driver.verify_connectivity()
            print("Connected to Neo4j database")
        except Exception as e:
            print(f"Failed to connect to Neo4j database: {e}")
            raise

    def close(self):
        if self.driver:
            self.driver.close()
            print("Neo4j connection closed")

    def execute_query(self, query, parameters=None):
        try:
            with self.driver.session() as session:
                result = session.run(query, parameters=parameters if parameters else {})
                return [record.data() for record in result]
        except ServiceUnavailable as e:
            print(f"Neo4j service unavailable: {e}")
            # Try to reconnect
            self._connect()
            raise
        except Exception as e:
            print(f"Query execution error: {e}")
            raise

    # Get summary statistics for all sensor readings
    def get_sensor_stats(self):
        query = """
        MATCH (n:SensorReading)
        RETURN 
          count(n) as totalReadings,
          min(n.temperature) as minTemp,
          max(n.temperature) as maxTemp,
          avg(n.temperature) as avgTemp,
          min(n.humidity) as minHumidity,
          max(n.humidity) as maxHumidity,
          avg(n.humidity) as avgHumidity,
          min(n.pressure) as minPressure,
          max(n.pressure) as maxPressure,
          avg(n.pressure) as avgPressure,
          min(n.gas) as minGas,
          max(n.gas) as maxGas,
          avg(n.gas) as avgGas
        """
        return self.execute_query(query)

    # Get classification distribution for time periods
    def get_classification_distribution(self):
        query = """
        MATCH (tg:TimeGroup)<-[:BELONGS_TO_TIME_GROUP]-(s:SensorReading)-[r:HAS_TEMPERATURE_CLASS|HAS_HUMIDITY_CLASS|HAS_GAS_CLASS]->(c:Classification)
        WITH tg.name as timeGroup, type(r) as sensorType, c.name as classification, count(*) as count
        RETURN timeGroup, sensorType, classification, count
        ORDER BY timeGroup, sensorType, 
          CASE classification
            WHEN 'High' THEN 1
            WHEN 'Medium' THEN 2
            WHEN 'Low' THEN 3
          END
        """
        return self.execute_query(query)

    # Get temperature distribution
    def get_temperature_distribution(self):
        query = """
        MATCH (n:SensorReading)
        WITH n.temperature as temp
        RETURN 
          CASE 
            WHEN temp < 29.5 THEN "< 29.5°C"
            WHEN temp >= 29.5 AND temp < 29.7 THEN "29.5-29.7°C"
            WHEN temp >= 29.7 AND temp < 29.9 THEN "29.7-29.9°C"
            WHEN temp >= 29.9 AND temp < 30.1 THEN "29.9-30.1°C"
            ELSE ">= 30.1°C"
          END as tempRange,
          count(*) as readingCount
        ORDER BY tempRange
        """
        return self.execute_query(query)

    # Get sample data for each time period
    def get_sample_readings(self):
        query = """
        MATCH (tg:TimeGroup)<-[:BELONGS_TO_TIME_GROUP]-(s:SensorReading)
        WITH tg.name as timeGroup, collect(s) as readings
        RETURN timeGroup, readings[0] as sampleReading
        ORDER BY 
          CASE timeGroup
            WHEN 'Early Readings' THEN 1
            WHEN 'Middle Readings' THEN 2
            WHEN 'Late Readings' THEN 3
          END
        """
        return self.execute_query(query)
