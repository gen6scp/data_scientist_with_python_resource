## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

import section1_001_exploring_missing_data
from section1_001_exploring_missing_data import students

sys.stdout = org_stdout


# Convert 'grades' column to integers
students['grades'] = students['grades'].astype('Int64')
print(students.dtypes)
