import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Figure object
fig = plt.figure()

# Data: correlation matrix
data = np.random.rand(10, 10)
corr_matrix = np.corrcoef(data)

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Customizing the plot
plt.title('Correlation Heatmap')

# Save the plot
plt.plot()
fig.savefig('plots/heatmap.png', transparent=True)

