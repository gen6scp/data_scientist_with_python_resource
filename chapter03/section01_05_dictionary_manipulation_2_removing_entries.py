## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section1_02_creating_a_dictionary import employee_dict 

sys.stdout = org_stdout


# Remove Bob from the dictionary
del employee_dict['Bob']

# Print the modified dictionary
print(employee_dict)
