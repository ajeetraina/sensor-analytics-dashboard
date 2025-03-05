import React from 'react';
import { 
  LineChart, Line, BarChart, Bar, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer 
} from 'recharts';

const Dashboard = ({ data }) => {
  // Extract data for visualization
  const { classificationData, trendData, stackedBarData } = data;

  // Colors for classification
  const COLORS = {
    High: '#ff4d4d',
    Medium: '#ffa64d',
    Low: '#4da6ff'
  };

  return (
    <div className="flex flex-col gap-6 p-4 bg-gray-50">
      <h1 className="text-2xl font-bold text-center">Neo4j Sensor Classification Analysis</h1>
      
      {/* Graph model visualization */}
      <div className="bg-white p-4 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-2">Neo4j Graph Model</h2>
        <div className="flex flex-col items-center">
          <div className="flex justify-center space-x-8 mb-6">
            <div className="border border-gray-300 rounded-lg p-3 text-center bg-gray-100">
              <div className="font-semibold">TimeGroup</div>
              <div>Early Readings</div>
              <div>Middle Readings</div>
              <div>Late Readings</div>
            </div>
            <div className="border border-gray-300 rounded-lg p-3 text-center bg-gray-100">
              <div className="font-semibold">Classification</div>
              <div className="text-red-500">High</div>
              <div className="text-orange-500">Medium</div>
              <div className="text-blue-500">Low</div>
            </div>
          </div>
          <div className="border border-gray-300 rounded-lg p-3 text-center bg-gray-100 mb-4">
            <div className="font-semibold">SensorReading</div>
            <div>temperature, humidity, gas, pressure, timestamp</div>
          </div>
          <div className="flex justify-center space-x-8">
            <div className="text-center">
              <div className="border-t-2 border-l-2 border-gray-400 h-8 w-16 ml-8"></div>
              <div className="text-sm">BELONGS_TO_TIME_GROUP</div>
            </div>
            <div className="text-center">
              <div className="flex space-x-4">
                <div>
                  <div className="border-t-2 border-gray-400 h-8 w-8"></div>
                  <div className="text-sm">HAS_TEMPERATURE_CLASS</div>
                </div>
                <div>
                  <div className="border-t-2 border-gray-400 h-8 w-8"></div>
                  <div className="text-sm">HAS_HUMIDITY_CLASS</div>
                </div>
                <div>
                  <div className="border-t-2 border-r-2 border-gray-400 h-8 w-16"></div>
                  <div className="text-sm">HAS_GAS_CLASS</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      {/* Classification Distribution by Time Group - Stacked Bar Chart */}
      <div className="bg-white p-4 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-2">Classification Distribution Over Time</h2>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={stackedBarData}
              margin={{ top: 20, right: 30, left: 20, bottom: 80 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis label={{ value: 'Count', angle: -90, position: 'insideLeft' }} />
              <Tooltip formatter={(value, name) => {
                const [sensorType, classification] = name.split('_');
                return [`${value} readings`, `${sensorType} - ${classification}`];
              }} />
              <Legend 
                layout="horizontal" 
                verticalAlign="bottom" 
                align="center"
                wrapperStyle={{ paddingTop: 20 }}
              />
              
              {/* Temperature */}
              <Bar dataKey="Temperature_High" stackId="Temperature" fill={COLORS.High} />
              <Bar dataKey="Temperature_Medium" stackId="Temperature" fill={COLORS.Medium} />
              <Bar dataKey="Temperature_Low" stackId="Temperature" fill={COLORS.Low} />
              
              {/* Humidity */}
              <Bar dataKey="Humidity_High" stackId="Humidity" fill={COLORS.High} />
              <Bar dataKey="Humidity_Medium" stackId="Humidity" fill={COLORS.Medium} />
              <Bar dataKey="Humidity_Low" stackId="Humidity" fill={COLORS.Low} />
              
              {/* Gas */}
              <Bar dataKey="Gas_High" stackId="Gas" fill={COLORS.High} />
              <Bar dataKey="Gas_Medium" stackId="Gas" fill={COLORS.Medium} />
              <Bar dataKey="Gas_Low" stackId="Gas" fill={COLORS.Low} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      
      {/* Sensor Classification Trends */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Temperature Classification Trend */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Temperature Classifications</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                data={trendData}
                margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="Temperature_High" stroke={COLORS.High} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Temperature_Medium" stroke={COLORS.Medium} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Temperature_Low" stroke={COLORS.Low} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
        
        {/* Humidity Classification Trend */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Humidity Classifications</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                data={trendData}
                margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="Humidity_High" stroke={COLORS.High} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Humidity_Medium" stroke={COLORS.Medium} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Humidity_Low" stroke={COLORS.Low} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
        
        {/* Gas Classification Trend */}
        <div className="bg-white p-4 rounded-lg shadow">
          <h2 className="text-xl font-semibold mb-2">Gas Classifications</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart
                data={trendData}
                margin={{ top: 5, right: 5, left: 5, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="Gas_High" stroke={COLORS.High} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Gas_Medium" stroke={COLORS.Medium} activeDot={{ r: 8 }} />
                <Line type="monotone" dataKey="Gas_Low" stroke={COLORS.Low} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Pie charts for each time period */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {["Early Readings", "Middle Readings", "Late Readings"].map((timeGroup, idx) => (
          <div key={idx} className="bg-white p-4 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-2">{timeGroup}</h2>
            <div className="h-64">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={classificationData.filter(d => d.timeGroup === timeGroup)}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="count"
                    nameKey="sensorType"
                    label={({ sensorType, classification, count, percent }) => 
                      `${sensorType} ${classification}: ${(percent * 100).toFixed(0)}%`
                    }
                  >
                    {classificationData.filter(d => d.timeGroup === timeGroup).map((entry, index) => (
                      <Cell 
                        key={`cell-${index}`} 
                        fill={COLORS[entry.classification]}
                        stroke={entry.sensorType === "Temperature" ? "#e60000" : 
                               entry.sensorType === "Humidity" ? "#006600" : "#000099"}
                        strokeWidth={2}
                      />
                    ))}
                  </Pie>
                  <Tooltip formatter={(value, name, props) => {
                    return [`${value} readings`, `${props.payload.sensorType} - ${props.payload.classification}`];
                  }} />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        ))}
      </div>

      {/* Summary Analysis */}
      <div className="bg-white p-4 rounded-lg shadow">
        <h2 className="text-xl font-semibold mb-4">Classification Analysis Summary</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-red-50 p-4 rounded-lg border border-red-200">
            <h3 className="font-semibold text-lg mb-2">Temperature Trend</h3>
            <ul className="list-disc pl-5 space-y-1">
              <li>Early: Mostly Low (72) & Medium (29)</li>
              <li>Middle: Mostly Low (69) & Medium (31)</li>
              <li>Late: Dramatic shift to High (109)</li>
              <li><span className="font-semibold">Conclusion:</span> Clear warming trend</li>
            </ul>
          </div>
          <div className="bg-blue-50 p-4 rounded-lg border border-blue-200">
            <h3 className="font-semibold text-lg mb-2">Humidity Trend</h3>
            <ul className="list-disc pl-5 space-y-1">
              <li>Early: All High (101)</li>
              <li>Middle: Mostly High (85) with some Medium (15)</li>
              <li>Late: Shift to Medium (48) & Low (78)</li>
              <li><span className="font-semibold">Conclusion:</span> Clear drying trend</li>
            </ul>
          </div>
          <div className="bg-green-50 p-4 rounded-lg border border-green-200">
            <h3 className="font-semibold text-lg mb-2">Gas Trend</h3>
            <ul className="list-disc pl-5 space-y-1">
              <li>Early: Mix of Low (23), Medium (44), & High (30)</li>
              <li>Middle: All High (100)</li>
              <li>Late: All High (126)</li>
              <li><span className="font-semibold">Conclusion:</span> Dramatic gas increase</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
