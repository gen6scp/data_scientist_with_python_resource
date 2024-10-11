## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section1_02_creating_a_dictionary import employee_dict 

sys.stdout = org_stdout


# Adding a new employee
employee_dict['Eve'] = 'Consultant'

# Updating an existing entry
employee_dict['Alice'] = 'Senior Engineer'

# Print the updated dictionary
print(employee_dict)
