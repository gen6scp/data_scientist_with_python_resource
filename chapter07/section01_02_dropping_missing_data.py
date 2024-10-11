## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_01_checking_column_types import ufo, pd

sys.stdout = org_stdout


# Display the count of missing values
print("* Missing values count per column:")
print(ufo.isnull().sum())

# Plot the distribution of the missing values
import seaborn as sns
import matplotlib.pyplot as plt
fig = plt.figure()
sns.heatmap(ufo.isnull(), cmap='viridis', cbar=False, yticklabels=False)
plt.title('Missing Values in UFO dataset')
plt.plot()
fig.savefig('plots/dropping_missing_data.png')


# Drop rows with missing values
print("* Before dropping the missing values")
print(ufo.shape)
ufo_dropped = ufo.dropna()
print("* After dropping the missing values")
print(ufo_dropped.shape)

