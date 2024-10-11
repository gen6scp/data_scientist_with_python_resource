## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section5_019_identifying_areas_for_feature_engineering import purchases

sys.stdout = org_stdout

# Importing Local Encoder
from sklearn.preprocessing import LabelEncoder

# Label encode 'location' column
encoder = LabelEncoder()
purchases['location_encoded'] = encoder.fit_transform(purchases['location'])

print(purchases[['location', 'location_encoded']])
