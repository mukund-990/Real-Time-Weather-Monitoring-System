import unittest
from unittest.mock import patch
from src.visualization.data_visualizer import DataVisualizer
from datetime import date

class TestDataVisualizer(unittest.TestCase):
    @patch('matplotlib.pyplot.show')
    def test_plot_daily_summary(self, mock_show):
        test_date = date(2021, 6, 1)
        test_summary = {
            'Delhi': {'avg_temp': 25, 'max_temp': 30, 'min_temp': 20},
            'Mumbai': {'avg_temp': 28, 'max_temp': 32, 'min_temp': 24}
        }

        DataVisualizer.plot_daily_summary(test_date, test_summary)

        # Assert that plt.show() was called
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
