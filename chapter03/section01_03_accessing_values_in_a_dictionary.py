## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section1_02_creating_a_dictionary import employee_dict 

sys.stdout = org_stdout


# Access Bob's job title
print(employee_dict['Bob'])  # Output: Manager

# Print all employee names (keys)
print(employee_dict.keys())  # Output: dict_keys(['Alice', 'Bob', 'Charlie', 'David'])

# Print all job titles (values)
print(employee_dict.values())  # Output: dict_values(['Engineer', 'Manager', 'Designer', 'Analyst'])
