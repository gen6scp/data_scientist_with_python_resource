# Import packages
import pandas as pd
import matplotlib.pyplot as plt

# URL of the file
url = 'winequality-red.csv'

# Read the file into a DataFrame
df = pd.read_csv(url, sep=',')

# Print the head of the DataFrame
print(df.head())

# Plot the first column of df
fig = plt.figure()
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.plot()

fig.savefig('plots/local_wine.png')
