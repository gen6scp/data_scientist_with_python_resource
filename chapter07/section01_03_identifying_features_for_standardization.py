## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_02_dropping_missing_data import ufo, ufo_dropped, pd

sys.stdout = org_stdout


import numpy as np

# Convert the 'duration (seconds)' column to numeric and filter out non-positive values
ufo_dropped = ufo_dropped.copy()
ufo_dropped.loc[:, 'duration (seconds)'] = pd.to_numeric(ufo_dropped['duration (seconds)'], errors='coerce')
ufo_dropped = ufo_dropped[ufo_dropped['duration (seconds)'] > 0]

# Log normalize 'duration (seconds)' column
ufo_dropped.loc[:, 'seconds_log'] = np.log(ufo_dropped['duration (seconds)'])


# Check variance
print("* Duration Variance")
print(ufo_dropped['duration (seconds)'].var())

print("* Duration Variance after Log Normalized")
print(ufo_dropped['seconds_log'].var())
