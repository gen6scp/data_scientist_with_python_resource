## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section5_019_identifying_areas_for_feature_engineering import purchases

sys.stdout = org_stdout

import pandas as pd

# One-hot encode 'location' column
location_dummies = pd.get_dummies(purchases['location'], prefix='location')

# Concatenate the new columns to the DataFrame
purchases = pd.concat([purchases, location_dummies], axis=1)

print(purchases)
