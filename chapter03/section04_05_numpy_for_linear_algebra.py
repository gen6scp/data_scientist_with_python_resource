import numpy as np

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("* Matrix Multiplication")
print(matrix_product)

# Transposing a matrix
transposed_matrix = matrix_a.T
print("\n* Transposed Matrix")
print(transposed_matrix)

