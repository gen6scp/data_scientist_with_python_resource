## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section4_03_filtering_data_with_pandas import pd, data, customers, loyal_customers

sys.stdout = org_stdout


# Combine conditions to filter customers with 2 to 4 purchases
selected_customers = customers[(customers['purchases'] >= 2) & (customers['purchases'] <= 4)]

# Print the selected DataFrame
print(selected_customers)
