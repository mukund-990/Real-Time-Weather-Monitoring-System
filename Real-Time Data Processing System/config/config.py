import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    API_KEY = os.getenv('fb753e1d6ee02a0614c4cd96acac38ee')
    API_BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    UPDATE_INTERVAL = 300  # 5 minutes in seconds
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    TEMPERATURE_UNIT = 'celsius'  # or 'fahrenheit'
    
    # Alerting thresholds
    MAX_TEMPERATURE_THRESHOLD = 35  # in Celsius
    CONSECUTIVE_ALERTS = 2

    # Database configuration (you can modify this based on your database choice)
    DATABASE_URL = 'sqlite:///weather_data.db'

# Add a print statement to check if the API key is loaded correctly
print(f"API Key: {Config.API_KEY}")
