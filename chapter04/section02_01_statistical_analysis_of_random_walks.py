# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Set the random seed for reproducibility
np.random.seed(42)

# Simulate multiple 1D random walks
num_walks = 500  # Number of walks
walk_length = 1000  # Number of steps per walk
final_positions = []  # List to store final positions

for i in range(num_walks):
    position = 0
    for j in range(walk_length):
        step = np.random.choice([-1, 1])
        position += step
    final_positions.append(position)

# Convert to NumPy array
final_positions = np.array(final_positions)

# Plot histogram of final positions
plt.hist(final_positions, bins=30, edgecolor='k', alpha=0.7)
plt.title("Distribution of Final Positions after 1000 Steps")
plt.xlabel("Final Position")
plt.ylabel("Frequency")

# Save the plot
plt.plot()
fig.savefig('plots/1d_random_walk_dist.png')

# Calculate mean squared displacement
mean_squared_displacement = np.mean(final_positions**2)
print(f"Mean Squared Displacement: {mean_squared_displacement}")
