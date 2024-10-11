import matplotlib.pyplot as plt
import numpy as np

# Figure object
fig = plt.figure()

# Data: products and revenue in two regions
products = ['Product A', 'Product B', 'Product C', 'Product D']
revenue_region1 = [20, 34, 30, 35]
revenue_region2 = [25, 32, 34, 40]

# Create index for bars
index = np.arange(len(products))
bar_width = 0.35

# Create bar plots
plt.bar(index, revenue_region1, bar_width, label='Region 1', color='blue', edgecolor='black')
plt.bar(index + bar_width, revenue_region2, bar_width, label='Region 2', color='green', edgecolor='black')

# Customizing the plot
plt.title('Revenue by Product and Region')
plt.xlabel('Product')
plt.ylabel('Revenue (in thousand dollars)')
plt.xticks(index + bar_width / 2, products)
plt.legend()

# Save the plot
plt.plot()
fig.savefig('plots/grouped_bar.png')
