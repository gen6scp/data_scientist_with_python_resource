import matplotlib.pyplot as plt
import numpy as np

# Figure object
fig = plt.figure()

# Data: daily sales in a store over a month
daily_sales = [220, 240, 250, 300, 310, 330, 350, 360, 370, 400, 410, 430, 440, 450, 460, 480, 490, 500, 520, 540, 550, 560, 580, 590, 600, 610, 620, 630, 640, 650]

# Create a box plot
plt.boxplot(daily_sales, vert=False, patch_artist=True, notch=True, boxprops=dict(facecolor='lightblue'))

# Customizing the plot
plt.title('Distribution of Daily Sales')
plt.xlabel('Sales (in dollars)')

# Highlighting the mean
plt.axvline(np.mean(daily_sales), color='red', linestyle='dashed', linewidth=1)
plt.text(np.mean(daily_sales) + 10, 1.1, 'Mean', color='red')

# Save the plot
plt.plot()
fig.savefig('plots/box.png')

