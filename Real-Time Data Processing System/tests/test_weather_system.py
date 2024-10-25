import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.api.openweathermap import OpenWeatherMapAPI
from src.data.aggregator import WeatherDataAggregator
from src.alerts.alert_system import AlertSystem
from src.config.config import Config

class TestWeatherSystem(unittest.TestCase):

    def setUp(self):
        self.api = OpenWeatherMapAPI()
        self.aggregator = WeatherDataAggregator()
        self.alert_system = AlertSystem()

    @patch('src.api.openweathermap.aiohttp.ClientSession.get')
    async def test_api_data_retrieval(self, mock_get):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.json.return_value = {
            "main": {"temp": 298.15},
            "weather": [{"main": "Clear"}]
        }
        mock_get.return_value.__aenter__.return_value = mock_response

        data = await self.api.get_weather_data("TestCity")
        self.assertIsNotNone(data)
        self.assertEqual(data['main']['temp'], 298.15)

    def test_temperature_conversion(self):
        kelvin = 300
        celsius = self.api.kelvin_to_celsius(kelvin)
        self.assertAlmostEqual(celsius, 26.85, places=2)

    def test_daily_summary_calculation(self):
        today = datetime.now().date()
        self.aggregator.add_weather_data("TestCity", today, 25, "Sunny")
        self.aggregator.add_weather_data("TestCity", today, 30, "Clear")
        self.aggregator.add_weather_data("TestCity", today, 20, "Cloudy")

        date, summary = self.aggregator.get_daily_summary()
        self.assertEqual(date, today)
        self.assertEqual(summary["TestCity"]["avg_temp"], 25)
        self.assertEqual(summary["TestCity"]["max_temp"], 30)
        self.assertEqual(summary["TestCity"]["min_temp"], 20)
        self.assertEqual(summary["TestCity"]["dominant_condition"], "Sunny")

    def test_alert_triggering(self):
        Config.ALERT_THRESHOLDS["TestCity"] = 35
        self.assertTrue(self.alert_system.check_alerts("TestCity", 36))
        self.assertTrue(self.alert_system.check_alerts("TestCity", 36))  # Second consecutive alert
        self.assertFalse(self.alert_system.check_alerts("TestCity", 34))  # Reset

if __name__ == '__main__':
    unittest.main()