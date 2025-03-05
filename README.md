# Sensor Analytics Dashboard

A real-time analytics dashboard for visualizing sensor data with Neo4j graph database integration. This project demonstrates classification of sensor readings (temperature, humidity, and gas) into High, Medium, and Low categories, with time-based trend analysis.

## Features

- **Real-time Visualization**: Live updates of sensor data via WebSocket connection
- **Graph Database Integration**: Neo4j for storing and querying sensor data
- **Classification System**: Categorizes readings as High, Medium, or Low
- **Time-based Analysis**: Groups readings into Early, Middle, and Late periods
- **Interactive Charts**: Multiple visualization types for different perspectives
- **Architecture Diagram**: Built-in system architecture visualization with Mermaid.js
- **Containerized Deployment**: Easy setup with Docker Compose

## Technology Stack

### Frontend
- **Framework**: Next.js with Vite
- **UI Library**: React
- **Visualization**: Recharts
- **Real-time**: Socket.IO client
- **Styling**: TailwindCSS
- **Diagramming**: Mermaid.js

### Backend
- **Framework**: Flask (Python)
- **WebSocket**: Flask-SocketIO
- **Database Access**: Neo4j Python Driver
- **API**: RESTful endpoints + WebSocket events

### Database
- **Neo4j**: Graph database for sensor data and relationships

### Deployment
- **Docker**: Containerized application services
- **Docker Compose**: Multi-container orchestration

## Quick Start

### Prerequisites
- Docker and Docker Compose installed
- Git for cloning the repository

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ajeetraina/sensor-analytics-dashboard.git
   cd sensor-analytics-dashboard
   ```

2. Start the application:
   ```bash
   docker-compose up -d
   ```

3. Access the dashboard:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Neo4j Browser: [http://localhost:7474](http://localhost:7474) (user: neo4j, password: password)

## Usage

### Viewing the Dashboard

Once the application is running, you can access the dashboard at [http://localhost:3000](http://localhost:3000). The dashboard includes:

- Neo4j graph model visualization
- Classification distribution charts
- Trend line charts for each sensor metric
- Time period breakdown pie charts
- Summary analysis of observed trends

### Viewing the Architecture

Click the "Show Architecture" button in the header to see a diagram of the system architecture, showing how the frontend, backend, and database components interact.

### Exploring Neo4j Data

You can explore the raw sensor data and graph structure using the Neo4j Browser at [http://localhost:7474](http://localhost:7474).

Login credentials:
- Username: `neo4j`
- Password: `password`

Useful Cypher queries to try:

```cypher
// View all sensor readings with their classifications
MATCH (s:SensorReading)-[r:HAS_TEMPERATURE_CLASS|HAS_HUMIDITY_CLASS|HAS_GAS_CLASS]->(c:Classification)
RETURN s, r, c LIMIT 100;

// Get distribution of classifications
MATCH (tg:TimeGroup)<-[:BELONGS_TO_TIME_GROUP]-(s:SensorReading)-[r:HAS_TEMPERATURE_CLASS|HAS_HUMIDITY_CLASS|HAS_GAS_CLASS]->(c:Classification)
WITH tg.name as timeGroup, type(r) as sensorType, c.name as classification, count(*) as count
RETURN timeGroup, sensorType, classification, count
ORDER BY timeGroup, sensorType, classification;
```

## Development

### Project Structure

```
├── frontend/          # Next.js with Vite React frontend
│   ├── src/           # React components and application code
│   ├── package.json   # Frontend dependencies
│   └── vite.config.js # Vite configuration
├── backend/           # Python Flask API backend
│   ├── app.py         # Main Flask application
│   ├── neo4j_connector.py # Neo4j database connector
│   ├── data_processor.py  # Data processing logic
│   └── requirements.txt   # Python dependencies
├── docker/            # Docker configuration files
│   ├── frontend.Dockerfile     # Frontend container config
│   ├── backend.Dockerfile      # Backend container config
│   └── neo4j/                  # Neo4j initialization
├── docs/              # Documentation
└── docker-compose.yml # Docker Compose configuration
```

### Running in Mock Mode

If you don't want to use Neo4j or want to test without a database connection, you can use mock mode:

1. Edit the `docker-compose.yml` file and set the environment variable for the backend service:
   ```yaml
   environment:
     - USE_MOCK_DATA=true
   ```

2. Restart the containers:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

### Local Development

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

#### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

## Documentation

Detailed documentation is available in the `docs/` directory:

- [Architecture Overview](docs/architecture.md)
- [Dashboard Guide](docs/dashboard.md)
- [Deployment Guide](docs/deployment.md)
- [Testing Guide](docs/testing.md)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## Use Cases for Electric Scooter Testing

This dashboard can be adapted for electric scooter testing in several ways:

1. **Battery Performance Monitoring**: Track temperature and voltage values during charge/discharge cycles
2. **Environmental Testing**: Analyze scooter component performance under varying temperature and humidity conditions
3. **Motor Efficiency Analysis**: Monitor current draw and temperature patterns during operation
4. **Vibration Testing**: Classify vibration patterns to identify potential mechanical issues
5. **Quality Control**: Test each scooter against established thresholds as it comes off the production line

The Neo4j graph structure enables complex relationship analysis that can reveal patterns between component sources, environmental conditions, and performance metrics.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
