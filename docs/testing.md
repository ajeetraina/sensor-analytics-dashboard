# Testing Guide

## Frontend Testing

### Manual Testing

1. **Basic Functionality**
   - Verify the dashboard loads correctly
   - Check all charts and visualizations render
   - Test responsive design on different screen sizes

2. **Real-time Updates**
   - Confirm WebSocket connection is established
   - Verify charts update when new data is received
   - Test reconnection when connection is lost

3. **User Interactions**
   - Test tooltips on hover
   - Verify architecture diagram toggle button works
   - Check all interactive elements respond correctly

### Automated Testing (Future Implementation)

- Component testing with React Testing Library
- E2E testing with Cypress

## Backend Testing

### Manual Testing

1. **API Endpoints**
   - Test `/api/sensor-data` endpoint returns expected data
   - Verify error handling for invalid requests
   - Check CORS headers are properly set

2. **Socket.IO**
   - Confirm connections are accepted
   - Verify data emissions occur at regular intervals
   - Test error handling during data processing

3. **Neo4j Connection**
   - Verify connection to database is established
   - Test error handling for database connection issues
   - Check query execution and result processing

### Automated Testing (Future Implementation)

- Unit tests for data processing functions
- API tests with pytest
- Mock Neo4j connections for isolated testing

## Docker Testing

1. **Container Build**
   - Verify all containers build successfully
   - Check for correct environment variable propagation
   - Test volume mounting for development

2. **Container Interaction**
   - Confirm networking between containers
   - Verify frontend can reach backend API
   - Test backend connection to Neo4j

3. **Performance**
   - Check memory usage of each container
   - Monitor CPU usage during operation
   - Test with simulated load

## Mock Mode Testing

1. **Enabling Mock Mode**
   - Set `USE_MOCK_DATA=true` in environment variables
   - Verify backend serves mock data instead of querying Neo4j
   - Check real-time updates with mock data

2. **Data Consistency**
   - Verify mock data structure matches Neo4j data structure
   - Confirm all visualization components work with mock data
   - Check error handling in mock mode

## Regression Testing

Before submitting a PR, perform the following regression tests:

1. Start the application with Docker Compose
2. Verify frontend loads and displays data
3. Check all visualizations are working
4. Test real-time updates
5. Verify Neo4j integration or mock mode
6. Check for any console errors or warnings
