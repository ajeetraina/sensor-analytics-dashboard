# Contributing Guidelines

Thank you for your interest in contributing to the Sensor Analytics Dashboard! This document provides guidelines and instructions for contributing to this project.

## Development Setup

### Prerequisites

- Docker and Docker Compose
- Git
- Node.js (for local frontend development)
- Python 3.10+ (for local backend development)

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ajeetraina/sensor-analytics-dashboard.git
   cd sensor-analytics-dashboard
   ```

2. Start the development environment with Docker:
   ```bash
   docker-compose up -d
   ```

3. Access the application:
   - Frontend: http://localhost:3000
   - Neo4j Browser: http://localhost:7474 (user: neo4j, password: password)

## Project Structure

- `frontend/`: Next.js with Vite React frontend
- `backend/`: Python Flask API backend
- `docker/`: Docker configuration files

## Development Workflow

### Making Changes

1. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes to the appropriate files

3. Test your changes by running the Docker environment:
   ```bash
   docker-compose down
   docker-compose up -d --build
   ```

4. Commit your changes with meaningful commit messages:
   ```bash
   git add .
   git commit -m "Add feature: your feature description"
   ```

5. Push your branch to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request on GitHub against the main branch

## Code Style and Standards

### Frontend

- Follow JavaScript/React best practices
- Use Tailwind CSS for styling
- Test components before submitting

### Backend

- Follow PEP 8 style guide for Python code
- Write docstrings for functions and classes
- Organize imports alphabetically

## Adding New Features

- For new frontend components, add them to the appropriate folders in `frontend/src/components/`
- For new API endpoints, update the appropriate files in `backend/`
- Update documentation as needed

## Testing

- Test your changes locally before submitting
- Ensure all existing features continue to work
- Include instructions for testing new features in your PR

## License

By contributing, you agree that your contributions will be licensed under the project's license.
