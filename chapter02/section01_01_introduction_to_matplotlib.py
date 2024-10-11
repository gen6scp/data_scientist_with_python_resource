import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 20, 25, 30]

# Basic line plot
plt.plot(x, y)

# Adding titles and labels
plt.title('Basic Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Save the plot
plt.plot()
fig.savefig('plots/introduction.png')

