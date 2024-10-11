## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section1_07_dictionary_of_dictionaries_nesting_dictionaries import employees_info

sys.stdout = org_stdout


# Loop through keys and values
for name, details in employees_info.items():
    print(f"{name} works as a {details['title']} in the {details['department']} department with {details['years_experience']} years of experience.")
