import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: daily sales in different store locations
sales_location1 = [220, 240, 250, 300, 310, 330, 350, 360, 370, 400]
sales_location2 = [410, 430, 440, 450, 460, 480, 490, 500, 520, 540]
sales_location3 = [550, 560, 580, 590, 600, 610, 620, 630, 640, 650]

# Combine data into a list
sales_data = [sales_location1, sales_location2, sales_location3]

# Create a box plot for each location
plt.boxplot(sales_data, patch_artist=True, notch=True, boxprops=dict(facecolor='lightgreen'))

# Customizing the plot
plt.title('Comparison of Daily Sales Across Store Locations')
plt.xlabel('Store Location')
plt.ylabel('Sales (in dollars)')
plt.xticks([1, 2, 3], ['Location 1', 'Location 2', 'Location 3'])

# Save the plot
plt.plot()
fig.savefig('plots/multi_box.png')
