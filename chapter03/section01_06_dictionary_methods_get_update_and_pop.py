## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section1_02_creating_a_dictionary import employee_dict 

sys.stdout = org_stdout


# Using get() to avoid KeyError
print(employee_dict.get('Frank', 'Not Found'))  # Output: Not Found

# Using update() to add multiple entries at once
employee_dict.update({'Frank': 'Technician', 'Grace': 'HR Specialist'})
print(employee_dict)

# Using pop() to remove and return a value
removed_employee = employee_dict.pop('Charlie')
print(f'Removed: {removed_employee}')  # Output: Removed: Designer
