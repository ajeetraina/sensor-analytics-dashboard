class DataProcessor:
    def __init__(self, neo4j_connector):
        self.neo4j = neo4j_connector

    def get_processed_data(self):
        """
        Process the data from Neo4j and format it for frontend visualization
        """
        try:
            # Get classification distribution data from Neo4j
            raw_classification_data = self.neo4j.get_classification_distribution()

            # Format classification data for React components
            classification_data = self._process_classification_data(raw_classification_data)
            
            # Generate trend data for line charts
            trend_data = self._generate_trend_data(raw_classification_data)
            
            # Generate stacked bar data
            stacked_bar_data = self._generate_stacked_bar_data(raw_classification_data)
            
            # Get sensor statistics
            sensor_stats = self.neo4j.get_sensor_stats()[0]  # Use only the first result
            
            # Get temperature distribution
            temp_distribution = self.neo4j.get_temperature_distribution()
            
            # Combine all data for the frontend
            return {
                'classificationData': classification_data,
                'trendData': trend_data,
                'stackedBarData': stacked_bar_data,
                'sensorStats': sensor_stats,
                'temperatureDistribution': temp_distribution
            }
        except Exception as e:
            print(f"Error processing Neo4j data: {e}")
            raise

    def _process_classification_data(self, raw_data):
        """
        Process raw classification data into format needed for React components
        """
        # Normalize sensorType names from relationship types
        sensor_type_map = {
            'HAS_TEMPERATURE_CLASS': 'Temperature',
            'HAS_HUMIDITY_CLASS': 'Humidity',
            'HAS_GAS_CLASS': 'Gas'
        }
        
        # Convert data to expected format for frontend
        result = []
        for item in raw_data:
            sensor_type = sensor_type_map.get(item['sensorType'], item['sensorType'])
            result.append({
                'timeGroup': item['timeGroup'],
                'sensorType': sensor_type,
                'classification': item['classification'],
                'count': item['count']
            })
        
        return result

    def _generate_trend_data(self, raw_data):
        """
        Generate trend data for line charts
        """
        # Create a map to organize data by time group
        trend_map = {
            'Early Readings': {'name': 'Early Readings', 'timeIndex': 0},
            'Middle Readings': {'name': 'Middle Readings', 'timeIndex': 1},
            'Late Readings': {'name': 'Late Readings', 'timeIndex': 2}
        }
        
        # Normalize sensorType names
        sensor_type_map = {
            'HAS_TEMPERATURE_CLASS': 'Temperature',
            'HAS_HUMIDITY_CLASS': 'Humidity',
            'HAS_GAS_CLASS': 'Gas'
        }
        
        # Fill in the data
        for item in raw_data:
            time_group = item['timeGroup']
            sensor_type = sensor_type_map.get(item['sensorType'], item['sensorType'])
            classification = item['classification']
            count = item['count']
            
            key = f"{sensor_type}_{classification}"
            trend_map[time_group][key] = count
        
        # Convert to list and sort by timeIndex
        return [trend_map[key] for key in sorted(trend_map.keys(), key=lambda k: trend_map[k]['timeIndex'])]

    def _generate_stacked_bar_data(self, raw_data):
        """
        Generate stacked bar data for the bar chart
        """
        # Group by time periods
        time_groups = ['Early Readings', 'Middle Readings', 'Late Readings']
        result = []
        
        # Normalize sensorType names
        sensor_type_map = {
            'HAS_TEMPERATURE_CLASS': 'Temperature',
            'HAS_HUMIDITY_CLASS': 'Humidity',
            'HAS_GAS_CLASS': 'Gas'
        }
        
        for time_group in time_groups:
            entry = {'name': time_group}
            
            # Find all classifications for this time group
            for item in raw_data:
                if item['timeGroup'] == time_group:
                    sensor_type = sensor_type_map.get(item['sensorType'], item['sensorType'])
                    classification = item['classification']
                    count = item['count']
                    
                    key = f"{sensor_type}_{classification}"
                    entry[key] = count
            
            result.append(entry)
        
        return result
