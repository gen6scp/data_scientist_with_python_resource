import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: products and average revenue (in thousand dollars)
products = ['Product A', 'Product B', 'Product C', 'Product D']
avg_revenue = [20, 34, 30, 35]

# Create a bar plot
plt.bar(products, avg_revenue, color='purple', edgecolor='black')

# Customizing the plot
plt.title('Average Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Average Revenue (in thousand dollars)')

# Adding values on top of bars
for i, v in enumerate(avg_revenue):
    plt.text(i, v + 0.5, str(v), ha='center', color='black', fontsize=12)

# Save the plot
plt.plot()
fig.savefig('plots/bar.png')
