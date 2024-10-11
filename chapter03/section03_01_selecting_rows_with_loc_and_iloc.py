## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section2_04_csv_to_dataframe_2 import weather_df

sys.stdout = org_stdout


# Select a single row by label (City)
print("* Select a single row by label (City)")
print(weather_df.loc['Chicago'])

# Select a single row by index position
print("\n* Select a single row by index position")
print(weather_df.iloc[2])

# Select multiple rows and columns using labels
print("\n* Select multiple rows and columns using labels")
print(weather_df.loc[['Chicago', 'Houston'], ['Max Temp (°C)', 'Precipitation (mm)']])

# Select multiple rows and columns using index positions
print("\n* Select multiple rows and columns using index positions")
print(weather_df.iloc[[2, 3], [0, 2]])
