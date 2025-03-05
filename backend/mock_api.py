from flask import Blueprint, jsonify
from mock_data import generate_mock_data

# Create Blueprint for mock API routes
mock_api = Blueprint('mock_api', __name__)

@mock_api.route('/api/sensor-data')
def get_mock_sensor_data():
    """Return mock data for testing without Neo4j"""
    return jsonify(generate_mock_data())
