import unittest
from unittest.mock import patch
from src.alerting.alert_system import AlertSystem
from config.config import Config

class TestAlertSystem(unittest.TestCase):
    def setUp(self):
        self.alert_system = AlertSystem()

    @patch('builtins.print')
    def test_temperature_threshold_alert(self, mock_print):
        # Test temperature below threshold
        self.alert_system.check_temperature_threshold(Config.MAX_TEMPERATURE_THRESHOLD - 1)
        mock_print.assert_not_called()

        # Test temperature above threshold, but not consecutive
        self.alert_system.check_temperature_threshold(Config.MAX_TEMPERATURE_THRESHOLD + 1)
        mock_print.assert_not_called()

        # Test temperature above threshold for consecutive times
        self.alert_system.check_temperature_threshold(Config.MAX_TEMPERATURE_THRESHOLD + 1)
        mock_print.assert_called_once()
        self.assertIn("High temperature alert", mock_print.call_args[0][0])

if __name__ == '__main__':
    unittest.main()
