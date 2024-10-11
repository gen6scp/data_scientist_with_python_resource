import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: ages of customers at two stores
ages_store1 = [18, 22, 25, 28, 30, 35, 38, 40, 45, 50, 55, 60, 65, 70, 75, 80]
ages_store2 = [20, 23, 27, 30, 32, 37, 40, 42, 47, 52, 58, 63, 68, 72, 72, 72]

# Create overlapping histograms
plt.hist(ages_store1, bins=8, alpha=0.5, label='Store 1', color='blue', edgecolor='black')
plt.hist(ages_store2, bins=8, alpha=0.5, label='Store 2', color='green', edgecolor='black')

# Customizing the plot
plt.title('Age Distribution of Customers by Store')
plt.xlabel('Age')
plt.ylabel('Number of Customers')

# Adding a legend
plt.legend()

# Save the plot
plt.plot()
fig.savefig('plots/distributions_with_histograms.png')

