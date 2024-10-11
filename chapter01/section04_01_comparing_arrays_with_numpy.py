# Import numpy library
import numpy as np

# Create age arrays for two groups
group_a = np.array([25, 32, 18, 40])
group_b = np.array([30, 28, 20, 35])

# Compare if ages in group_a are greater than or equal to 30
print(group_a >= 30)

# Compare if ages in group_a are less than those in group_b
print(group_a < group_b)
