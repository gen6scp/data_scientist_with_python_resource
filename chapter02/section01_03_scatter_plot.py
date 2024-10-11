import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: advertising budget and revenue
ad_budget = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
revenue = [15, 25, 35, 45, 50, 60, 65, 70, 80, 90]

# Create a scatter plot
plt.scatter(ad_budget, revenue, color='purple', alpha=0.5)

# Customizing the plot
plt.title('Advertising Budget vs Revenue')
plt.xlabel('Advertising Budget (in thousand dollars)')
plt.ylabel('Revenue (in thousand dollars)')

# Adding a trend line
import numpy as np
z = np.polyfit(ad_budget, revenue, 1)
p = np.poly1d(z)
plt.plot(ad_budget, p(ad_budget), "r--")

# Save the plot
plt.plot()
fig.savefig('plots/scatter.png')

