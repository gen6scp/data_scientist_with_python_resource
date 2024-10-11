# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Set the random seed for reproducibility
np.random.seed(42)

# Initialize parameters
steps = 1000  # Number of steps
position = [0, 0]  # Starting position at (0, 0)
walk = [position.copy()]  # List to store the positions

# Simulate the 2D random walk
for i in range(steps):
    direction = np.random.choice(["up", "down", "left", "right"])
    
    if direction == "up":
        position[1] += 1  # Move up in the y-direction
    elif direction == "down":
        position[1] -= 1  # Move down in the y-direction
    elif direction == "left":
        position[0] -= 1  # Move left in the x-direction
    elif direction == "right":
        position[0] += 1  # Move right in the x-direction
    
    walk.append(position.copy())

# Convert the walk list to a NumPy array for easier plotting
walk = np.array(walk)

# Plot the 2D Random Walk
plt.plot(walk[:, 0], walk[:, 1], marker="o", markersize=1)
plt.title("2D Random Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)

# Save the plot
plt.plot()
fig.savefig('plots/2d_random_walk.png')

