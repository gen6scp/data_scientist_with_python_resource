## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_06_text_vectorization import ufo, ufo_dropped, pd, np, desc_tfidf, vectorizer

sys.stdout = org_stdout


# Print
print("* Before: UFO Features - head()")
print(ufo_dropped.head())

# List of features to drop
to_drop = ['datetime', 'city', 'state', 'country', 'latitude', 'longitude', 'comments', 'duration (seconds)', 'duration (hours/min)', 'shape', 'date posted']
ufo_dropped = ufo_dropped.drop(columns=to_drop)

print("* After: UFO Features - head()")
print(ufo_dropped.head())
