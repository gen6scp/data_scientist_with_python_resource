# Import requests package
import requests

# Assign URL to variable
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=sneakers'

# Send the request and catch the response
r = requests.get(url)

# Print the text of the response
print(r.text)

