# Import pandas as pd
import pandas as pd

# Load the CSV file into a DataFrame
weather_df = pd.read_csv('weather_data.csv')

# Print the first 5 rows of the DataFrame
print(weather_df.head())
