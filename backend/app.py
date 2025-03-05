import os
from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from dotenv import load_dotenv
import time
import threading

# Import our modules
from neo4j_connector import Neo4jConnector
from data_processor import DataProcessor

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_key_change_in_production')

# Initialize Socket.IO with CORS support
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize Neo4j connector
neo4j_connector = Neo4jConnector(
    uri=os.getenv('NEO4J_URI', 'bolt://neo4j:7687'),
    user=os.getenv('NEO4J_USER', 'neo4j'),
    password=os.getenv('NEO4J_PASSWORD', 'password')
)

# Initialize data processor
data_processor = DataProcessor(neo4j_connector)

# Route for getting sensor data
@app.route('/api/sensor-data')
def get_sensor_data():
    try:
        # Process data from Neo4j
        processed_data = data_processor.get_processed_data()
        return jsonify(processed_data)
    except Exception as e:
        print(f"Error getting sensor data: {e}")
        return jsonify({'error': str(e)}), 500

# Socket.IO event for client connection
@socketio.on('connect')
def handle_connect():
    print('Client connected')

# Socket.IO event for client disconnection
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

# Background thread for sending real-time updates
stop_thread = False
def background_thread():
    global stop_thread
    while not stop_thread:
        try:
            # Get fresh data every 5 seconds
            processed_data = data_processor.get_processed_data()
            # Emit to all connected clients
            socketio.emit('sensor_update', processed_data)
            # Sleep for 5 seconds
            time.sleep(5)
        except Exception as e:
            print(f"Background thread error: {e}")
            time.sleep(5)  # Continue trying

# Start background thread
@app.before_first_request
def start_background_thread():
    global stop_thread
    stop_thread = False
    thread = threading.Thread(target=background_thread)
    thread.daemon = True
    thread.start()

# Cleanup when shutting down
@app.teardown_appcontext
def cleanup(error):
    global stop_thread
    stop_thread = True
    neo4j_connector.close()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    # Use gevent for better WebSocket performance
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
