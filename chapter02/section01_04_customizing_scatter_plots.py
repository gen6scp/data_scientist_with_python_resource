import matplotlib.pyplot as plt
import numpy as np

# Figure object
fig = plt.figure()

# Data: advertising budget, revenue, and regions
ad_budget = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
revenue = [15, 25, 35, 45, 50, 60, 65, 70, 80, 90]
regions = ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South']
sizes = np.array([100, 200, 300, 400, 100, 200, 300, 400, 100, 200])

# Map regions to colors
color_map = {'North': 'blue', 'South': 'green', 'East': 'red', 'West': 'orange'}
colors = [color_map[region] for region in regions]

# Create a scatter plot
plt.scatter(ad_budget, revenue, s=sizes, c=colors, alpha=0.6, edgecolor='black', linewidth=1.5)

# Customizing the plot
plt.title('Advertising Budget vs Revenue by Region')
plt.xlabel('Advertising Budget (in thousand dollars)')
plt.ylabel('Revenue (in thousand dollars)')

# Adding a trend line
z = np.polyfit(ad_budget, revenue, 1)
p = np.poly1d(z)
plt.plot(ad_budget, p(ad_budget), "r--")

# Adding a legend
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label='North'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='South'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='East'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=10, label='West')])


# Save the plot
plt.plot()
fig.savefig('plots/custom_scatter.png')

