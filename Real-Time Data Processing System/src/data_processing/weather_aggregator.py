from collections import Counter
from datetime import datetime

class WeatherAggregator:
    def __init__(self):
        self.daily_data = {}

    def add_weather_data(self, city, weather_data):
        date = datetime.fromtimestamp(weather_data['dt']).date()
        if date not in self.daily_data:
            self.daily_data[date] = {}
        if city not in self.daily_data[date]:
            self.daily_data[date][city] = []
        
        self.daily_data[date][city].append(weather_data)

    def get_daily_summary(self, date):
        summary = {}
        for city, data_list in self.daily_data.get(date, {}).items():
            temps = [d['main']['temp'] for d in data_list]
            conditions = [d['weather'][0]['main'] for d in data_list]
            
            summary[city] = {
                'avg_temp': sum(temps) / len(temps),
                'max_temp': max(temps),
                'min_temp': min(temps),
                'dominant_condition': Counter(conditions).most_common(1)[0][0]
            }
        return summary
