# Import pandas as pd
import pandas as pd

# Load CSV and set the City column as the index
weather_df = pd.read_csv('weather_data.csv', index_col='City')

# Print the updated DataFrame
print(weather_df)
