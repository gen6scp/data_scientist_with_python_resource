## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section2_04_csv_to_dataframe_2 import weather_df

sys.stdout = org_stdout


# Add a new column with the average temperature
weather_df['Average Temp (°C)'] = (weather_df['Max Temp (°C)'] + weather_df['Min Temp (°C)']) / 2
print("* Add a new column with the average temperature")
print(weather_df)

# Delete the Min Temp (°C) column
weather_df.drop('Min Temp (°C)', axis=1, inplace=True)
print("\n* Delete the Min Temp (°C) column")
print(weather_df)
