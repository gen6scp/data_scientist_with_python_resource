import matplotlib.pyplot as plt
import numpy as np

# Figure object
fig = plt.figure()

# Data: ages of customers
ages = [18, 20, 22, 25, 28, 30, 35, 38, 40, 45, 48, 50, 55, 58, 60, 62, 65, 68, 70, 72, 75, 78, 80]

# Create a histogram with custom bins and colors
plt.hist(ages, bins=8, color='skyblue', edgecolor='black')

# Customizing the plot
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Number of Customers')

# Adding a vertical line for the mean age
mean_age = np.mean(ages)
plt.axvline(mean_age, color='red', linestyle='dashed', linewidth=1)
plt.text(mean_age + 1, 5, 'Mean Age: {:.2f}'.format(mean_age), color='red')

# Save the plot
plt.plot()
fig.savefig('plots/histogram.png')

