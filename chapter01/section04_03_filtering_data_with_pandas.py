# Import pandas library
import pandas as pd

# Create a DataFrame
data = {'customer_id': [1, 2, 3, 4, 5],
        'purchases': [2, 5, 3, 1, 4]}
customers = pd.DataFrame(data)

# Filter customers who made more than 3 purchases
loyal_customers = customers[customers['purchases'] > 3]

# Print the filtered DataFrame
print(loyal_customers)
