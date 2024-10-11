# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Set the random seed for reproducibility
np.random.seed(42)

# Initialize parameters
steps = 1000  # Number of steps
position = 0  # Starting position
walk = [position]  # List to store the positions

# Simulate the random walk
for i in range(steps):
    step = np.random.choice([-1, 1])  # Choose randomly between -1 (backward) or 1 (forward)
    position += step
    walk.append(position)

# Plot the 1D Random Walk
plt.plot(walk)
plt.title("1D Random Walk")
plt.xlabel("Steps")
plt.ylabel("Position")

# Save the plot
plt.plot()
fig.savefig('plots/1d_random_walk.png')
