// Create classification nodes
CREATE (high:Classification {name: 'High'});
CREATE (medium:Classification {name: 'Medium'});
CREATE (low:Classification {name: 'Low'});

// Create time period nodes
CREATE (early:TimeGroup {name: 'Early Readings'});
CREATE (middle:TimeGroup {name: 'Middle Readings'});
CREATE (late:TimeGroup {name: 'Late Readings'});

// Create some sample sensor readings
// Early readings
WITH range(1, 20) AS ids
UNWIND ids AS id
CREATE (s:SensorReading {
  id: id,
  temperature: 29.5 + rand() * 0.1,
  humidity: 37.0 + rand() * 0.5,
  pressure: 912.9 + rand() * 0.1,
  gas: 2000 + id * 500,
  timestamp: 1741183389 + id * 5
});

// Middle readings
WITH range(21, 40) AS ids
UNWIND ids AS id
CREATE (s:SensorReading {
  id: id,
  temperature: 29.6 + rand() * 0.2,
  humidity: 36.0 + rand() * 0.5,
  pressure: 913.0 + rand() * 0.1,
  gas: 12000 + id * 800,
  timestamp: 1741184000 + (id-20) * 5
});

// Late readings
WITH range(41, 60) AS ids
UNWIND ids AS id
CREATE (s:SensorReading {
  id: id,
  temperature: 30.0 + rand() * 0.2,
  humidity: 33.0 + rand() * 1.0,
  pressure: 913.2 + rand() * 0.2,
  gas: 40000 + id * 400,
  timestamp: 1741185000 + (id-40) * 5
});

// Classify temperature readings
MATCH (s:SensorReading)
WITH s, s.temperature as temp
MATCH (c:Classification)
WHERE 
  (temp >= 29.9 AND c.name = 'High') OR
  (temp >= 29.6 AND temp < 29.9 AND c.name = 'Medium') OR
  (temp < 29.6 AND c.name = 'Low')
MERGE (s)-[:HAS_TEMPERATURE_CLASS]->(c);

// Classify humidity readings
MATCH (s:SensorReading)
WITH s, s.humidity as hum
MATCH (c:Classification)
WHERE 
  (hum >= 36.5 AND c.name = 'High') OR
  (hum >= 34.0 AND hum < 36.5 AND c.name = 'Medium') OR
  (hum < 34.0 AND c.name = 'Low')
MERGE (s)-[:HAS_HUMIDITY_CLASS]->(c);

// Classify gas readings
MATCH (s:SensorReading)
WITH s, s.gas as gas
MATCH (c:Classification)
WHERE 
  (gas >= 30000 AND c.name = 'High') OR
  (gas >= 10000 AND gas < 30000 AND c.name = 'Medium') OR
  (gas < 10000 AND c.name = 'Low')
MERGE (s)-[:HAS_GAS_CLASS]->(c);

// Connect to time groups
// Early readings (first 20)
MATCH (s:SensorReading)
WHERE s.id <= 20
MATCH (tg:TimeGroup {name: 'Early Readings'})
MERGE (s)-[:BELONGS_TO_TIME_GROUP]->(tg);

// Middle readings (21-40)
MATCH (s:SensorReading)
WHERE s.id > 20 AND s.id <= 40
MATCH (tg:TimeGroup {name: 'Middle Readings'})
MERGE (s)-[:BELONGS_TO_TIME_GROUP]->(tg);

// Late readings (41-60)
MATCH (s:SensorReading)
WHERE s.id > 40
MATCH (tg:TimeGroup {name: 'Late Readings'})
MERGE (s)-[:BELONGS_TO_TIME_GROUP]->(tg);
