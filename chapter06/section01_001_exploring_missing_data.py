import pandas as pd

# Sample data
data = {
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'address': [None, '123 Main St', None, '456 Maple Ave', '789 Elm St'],
    'grades': [88, 92, 85, None, 95]
}

students = pd.DataFrame(data)

# Check for missing values in 'address' column
missing_addresses = students['address'].isna().sum()
print(students)
print(f"Missing values in 'address' column: {missing_addresses}")
