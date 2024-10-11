# Import necessary packages
from urllib.request import urlretrieve
import pandas as pd

# URL of the file
url = 'https://github.com/gen6scp/becoming_a_data_scientist_resource/raw/main/chapter1/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read the file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=',')
print(df.head())
