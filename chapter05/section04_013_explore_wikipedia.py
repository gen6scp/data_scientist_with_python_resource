# Import package
import requests

# Assign URL to variable
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=germany'

# Send the request and catch the response
r = requests.get(url)

# Decode the JSON data into a dictionary
json_data = r.json()

# Print the Wikipedia page extract
wiki_extract = json_data['query']['pages']['11867']['extract']
print(wiki_extract)
