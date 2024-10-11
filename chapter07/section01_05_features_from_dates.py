## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_04_encoding_categorical_variables import ufo, ufo_dropped, pd, np

sys.stdout = org_stdout


# Print Before
print("* Type Before: " + str(ufo_dropped['datetime'].dtypes))

# Convert 'date' to datetime and extract month and year
ufo_dropped['datetime'] = pd.to_datetime(ufo_dropped['datetime'], errors='coerce')
ufo_dropped['month'] = ufo_dropped['datetime'].dt.month
ufo_dropped['year'] = ufo_dropped['datetime'].dt.year
ufo_dropped = ufo_dropped.dropna(subset=['month', 'year'])

# Print After
print("* Type After: " + str(ufo_dropped['datetime'].dtypes))

print("* Converted data")
print(ufo_dropped[['datetime', 'month', 'year']].head())
