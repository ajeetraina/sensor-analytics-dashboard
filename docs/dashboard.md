# Dashboard Guide

## Overview

The Sensor Analytics Dashboard visualizes sensor data using a classification system to categorize readings into High, Medium, and Low ranges. This guide explains the different components of the dashboard and how to interpret the visualizations.

## Dashboard Components

### Graph Model Visualization

The dashboard includes a visualization of the Neo4j graph model, showing how sensor readings are connected to classifications and time groups:

- **TimeGroup Nodes**: Early, Middle, and Late readings
- **Classification Nodes**: High, Medium, and Low
- **SensorReading Nodes**: Contains temperature, humidity, gas, and pressure data
- **Relationships**: Connect readings to classifications and time groups

### Classification Distribution

The stacked bar chart shows the distribution of classifications across time periods:

- X-axis: Time periods (Early, Middle, Late)
- Y-axis: Count of readings
- Colors: High (red), Medium (orange), Low (blue)
- Grouping: Temperature, Humidity, and Gas metrics

### Trend Visualization

The line charts show how classifications change over time for each metric:

- **Temperature Trends**: Shows warming trend with shift from Low to High
- **Humidity Trends**: Shows drying trend with shift from High to Low
- **Gas Trends**: Shows increasing concentration with shift to High

### Time Period Breakdown

Pie charts show the proportion of different classifications within each time period, making it easy to see the dominant classification for each metric at different points in time.

### Summary Analysis

The dashboard includes a textual summary of the trends observed in the data, highlighting key insights:

- Temperature warming trend
- Humidity drying trend
- Gas concentration increase

## Interpreting the Data

### Temperature Classifications

- **High**: ≥ 29.9°C
- **Medium**: 29.6-29.9°C
- **Low**: < 29.6°C

### Humidity Classifications

- **High**: ≥ 36.5%
- **Medium**: 34.0-36.5%
- **Low**: < 34.0%

### Gas Classifications

- **High**: ≥ 30,000 units
- **Medium**: 10,000-30,000 units
- **Low**: < 10,000 units

## Real-time Updates

The dashboard updates in real-time as new data becomes available:

1. New sensor readings are added to the Neo4j database
2. Backend processes the data and sends updates via WebSocket
3. Frontend visualizations refresh automatically

## Architecture View

Click the "Show Architecture" button in the header to view the system architecture diagram, which illustrates the components and data flow of the application.

## Customization (For Developers)

The dashboard can be customized by modifying the following files:

- **Frontend Components**: `frontend/src/components/`
- **Classification Thresholds**: `backend/data_processor.py`
- **Neo4j Data Model**: `docker/neo4j/init.cypher`

## Troubleshooting

### No Data Displayed

If no data is displayed, check:

1. Neo4j connection (if not using mock mode)
2. WebSocket connection status
3. Backend logs for errors

### Charts Not Updating

If charts are not updating in real-time:

1. Check your network connection
2. Verify WebSocket connection is established
3. Check browser console for errors

### Incorrect Data

If data appears incorrect:

1. Verify Neo4j database has proper data
2. Check classification thresholds
3. Review data processing logic in backend
