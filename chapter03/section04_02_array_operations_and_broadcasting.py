import numpy as np

# Element-wise addition
arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
sum_arr = arr_a + arr_b
print("* Element-wise addition")
print(sum_arr)  # Output: [5 7 9]

# Scalar multiplication (broadcasting)
scaled_arr = arr_a * 2
print("\n* Scalar multiplication (broadcasting)")
print(scaled_arr)  # Output: [2 4 6]

# Broadcasting with 2D arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_1d = np.array([10, 20, 30])
broadcasted_sum = arr_2d + arr_1d
print("\n* Broadcasting with 2D arrays")
print(broadcasted_sum)

