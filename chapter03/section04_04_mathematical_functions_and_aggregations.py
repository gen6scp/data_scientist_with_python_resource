import numpy as np

# Create a 2D array
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Summing all elements in an array
total_sum = np.sum(arr_2d)
print("total_sum = ", total_sum)  # Output: 450

# Finding the mean
mean_value = np.mean(arr_2d)
print("mean_value =", mean_value)  # Output: 50.0

# Finding the maximum value
max_value = np.max(arr_2d)
print("max_value = ", max_value)  # Output: 90

# Standard deviation
std_dev = np.std(arr_2d)
print("std_dev = ", std_dev)  # Output: 26.066

