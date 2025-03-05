# Architecture Overview

## System Components

The Sensor Analytics Dashboard consists of three main components:

1. **Frontend (Next.js + Vite + React)**
   - User interface for data visualization
   - Real-time updates via WebSocket connection
   - Interactive charts with Recharts
   - Responsive design with Tailwind CSS

2. **Backend (Python + Flask)**
   - REST API for data retrieval
   - Socket.IO server for real-time updates
   - Data processing and transformation
   - Neo4j database connector

3. **Database (Neo4j)**
   - Graph database for sensor data storage
   - Classification nodes (High, Medium, Low)
   - Time period grouping (Early, Middle, Late readings)
   - Relationship-based data structure

## Data Flow

1. Sensor data is stored in Neo4j with relationships to classification nodes
2. Backend queries Neo4j for sensor data and processes it for visualization
3. Frontend requests data via REST API or receives updates via WebSocket
4. Frontend visualizes data using charts and graphs

## Real-time Updates

The system uses Socket.IO for real-time updates:

1. Backend runs a background thread that queries Neo4j every 5 seconds
2. New data is processed and emitted to all connected clients
3. Frontend receives updates and refreshes visualizations without page reload

## Containerization

The entire system is containerized with Docker:

1. Frontend container: Next.js with Vite
2. Backend container: Python Flask
3. Neo4j container: Graph database with initialization script

Docker Compose orchestrates the containers and sets up networking.

## Graph Data Model

### Node Types

- **SensorReading**: Contains sensor data (temperature, humidity, gas, pressure, timestamp)
- **Classification**: Categorizes readings (High, Medium, Low)
- **TimeGroup**: Groups readings by time period (Early, Middle, Late)

### Relationship Types

- **HAS_TEMPERATURE_CLASS**: Links readings to temperature classification
- **HAS_HUMIDITY_CLASS**: Links readings to humidity classification
- **HAS_GAS_CLASS**: Links readings to gas classification
- **BELONGS_TO_TIME_GROUP**: Links readings to time group

## Mock Mode

The system can run in mock mode without requiring Neo4j:

1. Set `USE_MOCK_DATA=true` in environment variables
2. Backend serves pre-generated mock data matching Neo4j's structure
3. Real-time updates are simulated with mock data

This is useful for development and testing without a Neo4j instance.
