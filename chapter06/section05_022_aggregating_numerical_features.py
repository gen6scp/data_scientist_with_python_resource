## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section5_019_identifying_areas_for_feature_engineering import purchases

sys.stdout = org_stdout

# Aggregate total purchase amount by customer
total_purchase = purchases.groupby('customer_id')['purchase_amount'].sum().reset_index()
total_purchase.columns = ['customer_id', 'total_purchase_amount']

print(total_purchase)
