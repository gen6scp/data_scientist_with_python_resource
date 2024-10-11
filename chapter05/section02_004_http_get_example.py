# Import packages
from urllib.request import urlopen, Request

# Specify the URL
url = "https://example.com"

# Package the request
request = Request(url)

# Send the request and catch the response
response = urlopen(request)

# Print the type of the response
print(type(response))

# Be polite and close the response
response.close()
