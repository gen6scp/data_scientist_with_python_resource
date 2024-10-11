## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section4_03_filtering_data_with_pandas import pd, data, customers, loyal_customers

sys.stdout = org_stdout


# Add a new column 'loyal' based on purchases
customers['loyal'] = customers['purchases'] > 3

# Print the updated DataFrame
print(customers)
