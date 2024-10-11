## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section2_04_csv_to_dataframe_2 import weather_df

sys.stdout = org_stdout


# Filter rows where Max Temp (°C) is greater than 35
hot_cities = weather_df[weather_df['Max Temp (°C)'] > 35]
print(hot_cities)
