## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

import section1_001_exploring_missing_data
from section1_001_exploring_missing_data import students

sys.stdout = org_stdout


# Drop the 'address' column
students_dropped = students.drop(columns=['address'])

# Drop rows with missing 'grades'
students_dropped = students_dropped.dropna(subset=['grades'])

print(students_dropped)
