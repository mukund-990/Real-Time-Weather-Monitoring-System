# Real-Time Weather Monitoring System

## Overview
This project is a Python-based real-time weather monitoring system that fetches data from OpenWeatherMap API, processes it, and provides visualizations and alerts for multiple cities.

## Features
- Real-time weather data retrieval for multiple cities
- Daily weather summaries with temperature aggregates
- Identification of dominant weather conditions
- Historical weather trends visualization
- Configurable alert system for temperature thresholds
- Console-based alerts with optional email notifications

## Design Choices

1. **Modular Architecture**: 
   - The system is divided into separate modules (API, data aggregation, alerts, visualization) to enhance maintainability and allow for easy future expansions.

2. **Asynchronous API Calls**: 
   - We use Python's `asyncio` and `aiohttp` to make asynchronous API calls, allowing efficient retrieval of data for multiple cities concurrently.

3. **In-Memory Processing with Database Backup**: 
   - Recent data is kept in memory for fast processing, while historical data is stored in a SQLite database for persistence and long-term trend analysis.

4. **Configurable System**: 
   - Key parameters like cities to monitor, update intervals, and alert thresholds are centralized in a configuration file for easy customization.

5. **Visualization with Matplotlib**: 
   - We use Matplotlib for creating clear, informative visualizations of daily summaries and historical trends.

6. **Alerting System**: 
   - The system includes a flexible alerting mechanism that can be easily extended to support various notification methods.

## Prerequisites
- Python 3.7 or newer
- pip (Python package installer)

## Build Instructions

1. **Clone the Repository**
   ```
   git https://github.com/Vaibhavbasidoni/Real-Time-Data-Processing-System-for-Weather-Monitoring-with-Rollups-and-Aggregates.git
   cd Real-Time Data Processing System
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Configure the System**
   - Open `src/config/config.py` in a text editor
   - Replace `"your_api_key_here"` with your OpenWeatherMap API key
   - Modify the `CITIES` list to include the cities you want to monitor
   - Adjust `UPDATE_INTERVAL` and `ALERT_THRESHOLDS` as needed

5. **Run the System**
   ```
   python run.py
   ```

## Project Structure
Real-Time Data Processing System/
├── src/
│ ├── api/
│ │ └── openweathermap.py
│ ├── data/
│ │ └── aggregator.py
│ ├── alerts/
│ │ └── alert_system.py
│ ├── visualization/
│ │ └── data_visualizer.py
│ └── config/
│ └── config.py
├── tests/
│ └── test_weather_system.py
├── run.py
├── README.md
└── requirements.txt

## Configuration Options
- `API_KEY`: Your OpenWeatherMap API key
- `CITIES`: List of cities to monitor
- `UPDATE_INTERVAL`: Time between data updates (in seconds)
- `ALERT_THRESHOLDS`: Temperature thresholds for triggering alerts

## Running Tests
Execute the following command to run the test suite:  python -m unittest discover tests

## Extending the System
- To add new cities: Modify the `CITIES` list in `src/config/config.py`
- To change alert thresholds: Update `ALERT_THRESHOLDS` in `src/config/config.py`
- To add new data visualizations: Extend the `DataVisualizer` class in `src/visualization/data_visualizer.py`

## Troubleshooting
- Ensure your API key is correctly set in the configuration file
- Check your internet connection if you're experiencing data retrieval issues
- For visualization problems, ensure Matplotlib is correctly installed
