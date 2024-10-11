# Import package
import requests

# Assign URL to variable
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=sneakers'

# Send the request and catch the response
r = requests.get(url)

# Decode the JSON data into a dictionary
json_data = r.json()

# Print each key-value pair in the JSON data
for k in json_data.keys():
    print(k + ': ', json_data[k])
