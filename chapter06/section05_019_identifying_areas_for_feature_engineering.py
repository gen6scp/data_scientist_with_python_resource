import pandas as pd

data = {
    'customer_id': [1, 2, 3, 4, 5],
    'purchase_amount': [100, 150, 200, 130, 160],
    'purchase_date': ['2023-01-01', '2023-01-03', '2023-01-04', '2023-01-07', '2023-01-08'],
    'location': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles']
}
purchases = pd.DataFrame(data)

print(purchases)
