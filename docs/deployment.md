# Deployment Guide

## Local Deployment with Docker

### Prerequisites

- Docker and Docker Compose installed
- Git for cloning the repository

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ajeetraina/sensor-analytics-dashboard.git
   cd sensor-analytics-dashboard
   ```

2. Start the application:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Neo4j Browser: http://localhost:7474

4. Stop the application:
   ```bash
   docker-compose down
   ```

## Production Deployment

### Prerequisites

- Docker and Docker Compose installed on production server
- Domain name (optional)
- SSL certificates (recommended)

### Configuration for Production

1. Update environment variables for production:
   - Create a `.env` file in the project root
   - Set secure passwords for Neo4j
   - Configure appropriate secret keys

2. Update Docker Compose file if needed:
   - Adjust port mappings if required
   - Configure persistent volumes for Neo4j data

### Deployment Steps

1. Clone the repository on the production server:
   ```bash
   git clone https://github.com/ajeetraina/sensor-analytics-dashboard.git
   cd sensor-analytics-dashboard
   ```

2. Create and configure the `.env` file with production settings

3. Build and start the containers:
   ```bash
   docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
   ```

4. Verify the application is running:
   ```bash
   docker-compose ps
   ```

### SSL Configuration

For production deployments, it's recommended to set up SSL:

1. Obtain SSL certificates for your domain

2. Set up a reverse proxy (like Nginx or Traefik) to handle SSL termination

3. Configure the reverse proxy to forward requests to the application containers

### Monitoring and Maintenance

1. Monitor container logs:
   ```bash
   docker-compose logs -f
   ```

2. Check container status:
   ```bash
   docker-compose ps
   ```

3. Restart services if needed:
   ```bash
   docker-compose restart [service_name]
   ```

4. Update to new versions:
   ```bash
   git pull
   docker-compose down
   docker-compose up -d --build
   ```

## Scaling Considerations

### Backend Scaling

For higher loads, consider:

1. Implementing a load balancer for backend instances
2. Using a production-grade WSGI server like Gunicorn
3. Separating WebSocket servers from API servers

### Database Scaling

For Neo4j scaling:

1. Configure appropriate memory settings
2. Consider Neo4j clusters for higher availability
3. Implement regular backups of Neo4j data

### Containerization

For production container management:

1. Consider using Kubernetes for container orchestration
2. Implement container health checks
3. Set up auto-scaling based on load
