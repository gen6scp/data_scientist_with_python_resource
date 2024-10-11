## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section4_03_filtering_data_with_pandas import pd, data, customers, loyal_customers

sys.stdout = org_stdout


# Iterate over DataFrame rows
for index, row in customers.iterrows():
    print(f"Customer {row['customer_id']} made {row['purchases']} purchases.")
