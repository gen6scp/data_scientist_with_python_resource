# Import packages
import json
import pandas as pd
import requests

# Define the API key and URL
api_key = 'YOUR_OPEN_WEATHER_API_KEY'
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Send the request and catch the response
r = requests.get(url)

# Decode the JSON data
weather_data = r.json()

# Save JSON file
with open('weather.json', 'w') as f:
    json.dump(weather_data, f)

# Create a DataFrame
df = pd.DataFrame([weather_data])

# Print the head of the DataFrame
print(df.head())
