## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section5_019_identifying_areas_for_feature_engineering import purchases

sys.stdout = org_stdout

import pandas as pd

# Convert 'purchase_date' to datetime
purchases['purchase_date'] = pd.to_datetime(purchases['purchase_date'])

# Extract month and year
purchases['purchase_month'] = purchases['purchase_date'].dt.month
purchases['purchase_year'] = purchases['purchase_date'].dt.year

print(purchases[['purchase_date', 'purchase_month', 'purchase_year']])
