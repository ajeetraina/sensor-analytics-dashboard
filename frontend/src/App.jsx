import React, { useState, useEffect } from 'react';
import Dashboard from './components/Dashboard';
import ArchitectureDiagram from './components/ArchitectureDiagram';
import { io } from 'socket.io-client';
import axios from 'axios';

function App() {
  const [sensorData, setSensorData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [showArchitecture, setShowArchitecture] = useState(false);

  useEffect(() => {
    // Initial data fetch
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get('/api/sensor-data');
        setSensorData(response.data);
        setError(null);
      } catch (err) {
        console.error('Error fetching sensor data:', err);
        setError('Failed to load sensor data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    // Set up real-time updates with Socket.io
    const socket = io();
    
    socket.on('connect', () => {
      console.log('Connected to WebSocket server');
    });

    socket.on('sensor_update', (data) => {
      console.log('Received sensor update:', data);
      setSensorData(data);
    });

    socket.on('connect_error', (err) => {
      console.error('Socket connection error:', err);
      setError('Connection to real-time server failed. Data may not be up-to-date.');
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4 text-gray-700">Loading sensor data...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-center bg-red-50 p-6 rounded-lg border border-red-200 max-w-md">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-red-500 mx-auto" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <h2 className="text-xl font-bold text-red-700 mt-4">Error</h2>
          <p className="mt-2 text-gray-700">{error}</p>
          <button 
            className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
            onClick={() => window.location.reload()}
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8 flex justify-between items-center">
          <h1 className="text-2xl font-bold text-gray-900">Sensor Analytics Dashboard</h1>
          <button
            onClick={() => setShowArchitecture(!showArchitecture)}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
          >
            {showArchitecture ? 'Hide Architecture' : 'Show Architecture'}
          </button>
        </div>
      </header>
      <main>
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          {showArchitecture && <ArchitectureDiagram />}
          
          {sensorData ? (
            <Dashboard data={sensorData} />
          ) : (
            <div className="text-center p-12 bg-white rounded-lg shadow">
              <p>No sensor data available.</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
