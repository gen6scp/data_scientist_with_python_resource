## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section4_03_filtering_data_with_pandas import pd, data, customers, loyal_customers

sys.stdout = org_stdout


# Use apply to categorize customers based on their purchases
def categorize_customer(purchases):
    if purchases > 3:
        return 'High'
    elif purchases == 3:
        return 'Medium'
    else:
        return 'Low'

customers['category'] = customers['purchases'].apply(categorize_customer)

# Print the updated DataFrame
print(customers)
