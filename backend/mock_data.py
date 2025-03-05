# Helper script to generate mock data for testing when Neo4j isn't available

def generate_mock_data():
    """
    Generate mock data that matches the structure of the data from Neo4j
    """
    # Sample classification data
    classification_data = [
        # Early Readings
        { "timeGroup": "Early Readings", "sensorType": "Temperature", "classification": "High", "count": 0 },
        { "timeGroup": "Early Readings", "sensorType": "Temperature", "classification": "Medium", "count": 29 },
        { "timeGroup": "Early Readings", "sensorType": "Temperature", "classification": "Low", "count": 72 },
        { "timeGroup": "Early Readings", "sensorType": "Humidity", "classification": "High", "count": 101 },
        { "timeGroup": "Early Readings", "sensorType": "Humidity", "classification": "Medium", "count": 0 },
        { "timeGroup": "Early Readings", "sensorType": "Humidity", "classification": "Low", "count": 0 },
        { "timeGroup": "Early Readings", "sensorType": "Gas", "classification": "High", "count": 30 },
        { "timeGroup": "Early Readings", "sensorType": "Gas", "classification": "Medium", "count": 44 },
        { "timeGroup": "Early Readings", "sensorType": "Gas", "classification": "Low", "count": 23 },
        
        # Middle Readings
        { "timeGroup": "Middle Readings", "sensorType": "Temperature", "classification": "High", "count": 0 },
        { "timeGroup": "Middle Readings", "sensorType": "Temperature", "classification": "Medium", "count": 31 },
        { "timeGroup": "Middle Readings", "sensorType": "Temperature", "classification": "Low", "count": 69 },
        { "timeGroup": "Middle Readings", "sensorType": "Humidity", "classification": "High", "count": 85 },
        { "timeGroup": "Middle Readings", "sensorType": "Humidity", "classification": "Medium", "count": 15 },
        { "timeGroup": "Middle Readings", "sensorType": "Humidity", "classification": "Low", "count": 0 },
        { "timeGroup": "Middle Readings", "sensorType": "Gas", "classification": "High", "count": 100 },
        { "timeGroup": "Middle Readings", "sensorType": "Gas", "classification": "Medium", "count": 0 },
        { "timeGroup": "Middle Readings", "sensorType": "Gas", "classification": "Low", "count": 0 },
        
        # Late Readings
        { "timeGroup": "Late Readings", "sensorType": "Temperature", "classification": "High", "count": 109 },
        { "timeGroup": "Late Readings", "sensorType": "Temperature", "classification": "Medium", "count": 17 },
        { "timeGroup": "Late Readings", "sensorType": "Temperature", "classification": "Low", "count": 0 },
        { "timeGroup": "Late Readings", "sensorType": "Humidity", "classification": "High", "count": 0 },
        { "timeGroup": "Late Readings", "sensorType": "Humidity", "classification": "Medium", "count": 48 },
        { "timeGroup": "Late Readings", "sensorType": "Humidity", "classification": "Low", "count": 78 },
        { "timeGroup": "Late Readings", "sensorType": "Gas", "classification": "High", "count": 126 },
        { "timeGroup": "Late Readings", "sensorType": "Gas", "classification": "Medium", "count": 0 },
        { "timeGroup": "Late Readings", "sensorType": "Gas", "classification": "Low", "count": 0 },
    ]
    
    # Generate trend data
    trend_data = [
        {
            "name": "Early Readings",
            "timeIndex": 0,
            "Temperature_High": 0,
            "Temperature_Medium": 29,
            "Temperature_Low": 72,
            "Humidity_High": 101,
            "Humidity_Medium": 0,
            "Humidity_Low": 0,
            "Gas_High": 30,
            "Gas_Medium": 44,
            "Gas_Low": 23
        },
        {
            "name": "Middle Readings",
            "timeIndex": 1,
            "Temperature_High": 0,
            "Temperature_Medium": 31,
            "Temperature_Low": 69,
            "Humidity_High": 85,
            "Humidity_Medium": 15,
            "Humidity_Low": 0,
            "Gas_High": 100,
            "Gas_Medium": 0,
            "Gas_Low": 0
        },
        {
            "name": "Late Readings",
            "timeIndex": 2,
            "Temperature_High": 109,
            "Temperature_Medium": 17,
            "Temperature_Low": 0,
            "Humidity_High": 0,
            "Humidity_Medium": 48,
            "Humidity_Low": 78,
            "Gas_High": 126,
            "Gas_Medium": 0,
            "Gas_Low": 0
        }
    ]
    
    # Generate stacked bar data
    stacked_bar_data = [
        {
            "name": "Early Readings",
            "Temperature_High": 0,
            "Temperature_Medium": 29,
            "Temperature_Low": 72,
            "Humidity_High": 101,
            "Humidity_Medium": 0,
            "Humidity_Low": 0,
            "Gas_High": 30,
            "Gas_Medium": 44,
            "Gas_Low": 23
        },
        {
            "name": "Middle Readings",
            "Temperature_High": 0,
            "Temperature_Medium": 31,
            "Temperature_Low": 69,
            "Humidity_High": 85,
            "Humidity_Medium": 15,
            "Humidity_Low": 0,
            "Gas_High": 100,
            "Gas_Medium": 0,
            "Gas_Low": 0
        },
        {
            "name": "Late Readings",
            "Temperature_High": 109,
            "Temperature_Medium": 17,
            "Temperature_Low": 0,
            "Humidity_High": 0,
            "Humidity_Medium": 48,
            "Humidity_Low": 78,
            "Gas_High": 126,
            "Gas_Medium": 0,
            "Gas_Low": 0
        }
    ]
    
    # Generate sensor stats
    sensor_stats = {
        "totalReadings": 327,
        "minTemp": 29.42,
        "maxTemp": 30.2,
        "avgTemp": 29.77,
        "minHumidity": 31.03,
        "maxHumidity": 37.71,
        "avgHumidity": 35.77,
        "minPressure": 912.91,
        "maxPressure": 913.48,
        "avgPressure": 913.26,
        "minGas": 1992.27,
        "maxGas": 65110.74,
        "avgGas": 44289.33
    }
    
    # Generate temperature distribution
    temperature_distribution = [
        {"tempRange": "< 29.5°C", "readingCount": 13},
        {"tempRange": "29.5-29.7°C", "readingCount": 168},
        {"tempRange": "29.7-29.9°C", "readingCount": 37},
        {"tempRange": "29.9-30.1°C", "readingCount": 46},
        {"tempRange": ">= 30.1°C", "readingCount": 63}
    ]
    
    return {
        'classificationData': classification_data,
        'trendData': trend_data,
        'stackedBarData': stacked_bar_data,
        'sensorStats': sensor_stats,
        'temperatureDistribution': temperature_distribution
    }

if __name__ == "__main__":
    # Print mock data for testing
    import json
    print(json.dumps(generate_mock_data(), indent=2))
