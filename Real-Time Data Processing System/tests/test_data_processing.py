import unittest
from datetime import datetime, date
from src.data_processing.weather_aggregator import WeatherAggregator
from src.data_processing.temperature_converter import TemperatureConverter

class TestWeatherAggregator(unittest.TestCase):
    def setUp(self):
        self.aggregator = WeatherAggregator()

    def test_add_weather_data(self):
        test_data = {
            'main': {'temp': 25},
            'weather': [{'main': 'Clear'}],
            'dt': 1622555400
        }
        self.aggregator.add_weather_data('Delhi', test_data)
        
        # Check if data was added correctly
        self.assertIn(date(2021, 6, 1), self.aggregator.daily_data)
        self.assertIn('Delhi', self.aggregator.daily_data[date(2021, 6, 1)])
        self.assertEqual(len(self.aggregator.daily_data[date(2021, 6, 1)]['Delhi']), 1)

    def test_get_daily_summary(self):
        # Add some test data
        test_date = date(2021, 6, 1)
        self.aggregator.daily_data[test_date] = {
            'Delhi': [
                {'main': {'temp': 25}, 'weather': [{'main': 'Clear'}], 'dt': 1622555400},
                {'main': {'temp': 27}, 'weather': [{'main': 'Clear'}], 'dt': 1622566200},
                {'main': {'temp': 23}, 'weather': [{'main': 'Cloudy'}], 'dt': 1622577000}
            ]
        }

        summary = self.aggregator.get_daily_summary(test_date)

        # Check the summary
        self.assertIn('Delhi', summary)
        self.assertAlmostEqual(summary['Delhi']['avg_temp'], 25, places=1)
        self.assertEqual(summary['Delhi']['max_temp'], 27)
        self.assertEqual(summary['Delhi']['min_temp'], 23)
        self.assertEqual(summary['Delhi']['dominant_condition'], 'Clear')

class TestTemperatureConverter(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(273.15), 0, places=2)
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_celsius(373.15), 100, places=2)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_fahrenheit(273.15), 32, places=2)
        self.assertAlmostEqual(TemperatureConverter.kelvin_to_fahrenheit(373.15), 212, places=2)

    def test_convert_temperature(self):
        self.assertAlmostEqual(TemperatureConverter.convert_temperature(300, 'celsius'), 26.85, places=2)
        self.assertAlmostEqual(TemperatureConverter.convert_temperature(300, 'fahrenheit'), 80.33, places=2)
        
        with self.assertRaises(ValueError):
            TemperatureConverter.convert_temperature(300, 'invalid_unit')

if __name__ == '__main__':
    unittest.main()
