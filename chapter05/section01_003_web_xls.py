# Import packages
from urllib.request import urlretrieve
import pandas as pd

# URL of the file
url = 'https://github.com/gen6scp/data_scientist_with_python_resource/raw/main/chapter05/latitude.xlsx'
urlretrieve(url, 'latitude.xlsx')

# Read all sheets of the Excel file
xls = pd.read_excel('latitude.xlsx', sheet_name=None)

# Print the sheet names
print(xls.keys())

# Print the head of the first sheet using its name
print(xls['Sheet1'].head())
