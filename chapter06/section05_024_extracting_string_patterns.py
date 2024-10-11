import re
import pandas as pd

# Sample data
data = {
    'trail': ['Trail A', 'Trail B', 'Trail C'],
    'length': ['3.5 miles', '5 miles', '2.75 miles']
}
trails = pd.DataFrame(data)

# Function to extract mileage
def extract_mileage(length):
    match = re.search(r'\d+(\.\d+)?', length)
    if match:
        return float(match.group(0))

# Apply function
trails['mileage'] = trails['length'].apply(extract_mileage)

print(trails)
