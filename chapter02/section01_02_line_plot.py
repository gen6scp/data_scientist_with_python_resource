import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: years and revenue (in million dollars)
years = [2018, 2019, 2020, 2021, 2022]
revenue = [50, 55, 60, 68, 75]

# Create a line plot
plt.plot(years, revenue, marker='o', linestyle='-', color='blue')

# Adding a grid
plt.grid(True)

# Adding titles and labels
plt.title('Company Revenue Over Years')
plt.xlabel('Year')
plt.ylabel('Revenue (in million dollars)')

# Highlighting specific points
plt.text(2019, 55, 'Dip in Growth', fontsize=12, color='red')
plt.text(2022, 75, 'Record High', fontsize=12, color='green')

# Save the plot
plt.plot()
fig.savefig('plots/line.png')
