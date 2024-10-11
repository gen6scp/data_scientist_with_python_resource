# Import packages
import json
import requests

# Define the API key and URL
api_key = 'YOUR_OPEN_WEATHER_API_KEY'
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Send the request and catch the response
r = requests.get(url)

# Decode the JSON data
weather_data = r.json()

# Print each key-value pair in the JSON data
for k in weather_data.keys():
    print(k + ': ', weather_data[k])
