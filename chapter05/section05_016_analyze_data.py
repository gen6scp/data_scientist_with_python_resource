import json

# Read JSON file
with open('weather.json') as f:
    weather_data = json.load(f)

# Extract specific fields
temperature = weather_data['main']['temp']
humidity = weather_data['main']['humidity']
weather_description = weather_data['weather'][0]['description']

# Print the extracted information
print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")
print(f"Weather Description: {weather_description}")
