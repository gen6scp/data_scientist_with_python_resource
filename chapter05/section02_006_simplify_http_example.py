# Import package
import requests

# Specify the URL
url = "http://www.example.com"

# Send the request and catch the response
r = requests.get(url)

# Extract the response
text = r.text

# Print the HTML
print(text)
