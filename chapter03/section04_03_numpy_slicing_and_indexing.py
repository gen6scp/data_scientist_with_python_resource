import numpy as np

# Create a 2D array
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Accessing a specific element
print("* Accessing a specific element")
print(arr_2d[1, 2])  # Output: 60 (row index 1, column index 2)

# Slicing rows and columns
print("\* Slicing rows and columns")
print(arr_2d[:, 1])  # Output: [20 50 80] (second column)

# Slicing a submatrix
print("\n* Slicing a submatrix")
print(arr_2d[0:2, 1:3])  # Output: [[20 30], [50 60]]
