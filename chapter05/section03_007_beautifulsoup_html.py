# Import packages
import requests
from bs4 import BeautifulSoup

# Specify the URL
url = 'https://www.example.com'

# Package the request, send the request, and catch the response
r = requests.get(url)

# Extract the response as HTML
html_doc = r.text

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Prettify the BeautifulSoup object
pretty_soup = soup.prettify()

# Print the prettified HTML
print(pretty_soup)
