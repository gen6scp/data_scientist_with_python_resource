# Import packages
from urllib.request import urlopen, Request

# Specify the URL
url = "https://example.com"

# Package the request
request = Request(url)

# Send the request and catch the response
response = urlopen(request)

# Extract the response
html = response.read()

# Print the HTML
print(html)
