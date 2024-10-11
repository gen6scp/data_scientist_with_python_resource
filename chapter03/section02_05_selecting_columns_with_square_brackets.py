## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section2_04_csv_to_dataframe_2 import weather_df

sys.stdout = org_stdout


# Select the Max Temp (°C) column
max_temp = weather_df['Max Temp (°C)']
print("* Select the Max Temp (°C) column")
print(max_temp)

# Select multiple columns
temp_data = weather_df[['Max Temp (°C)', 'Min Temp (°C)']]
print("\n* Select multiple columns")
print(temp_data)
