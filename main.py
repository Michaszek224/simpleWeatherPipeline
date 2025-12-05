import pandas as pd
import time
import requests
import datetime
from sqlalchemy import create_engine

db_string = "postgresql://user:password@localhost:5432/mydatabase"
engine = create_engine(db_string)

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=52.2297&longitude=21.0122&current_weather=true"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_temp = data['current_weather']['temperature']
        wind_speed = data['current_weather']['windspeed']
        
        print(f"Current Temperature: {current_temp}°C")
        print(f"Wind Speed: {wind_speed} km/h")
        
        df = pd.DataFrame({
            'city': ['Warsaw'],
            'temperature': [current_temp],
            'wind_speed': [wind_speed],
            'timestamp': [datetime.datetime.now()]
        })
        return df
    else:
        print("Failed to retrieve weather data")
        return pd.DataFrame()


while True:
    df = get_weather()
    try:
        df.to_sql('air_quality', engine, if_exists='append', index=False)
        print("DataFrame written to database successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    time.sleep(60)

