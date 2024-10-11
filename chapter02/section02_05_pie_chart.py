import matplotlib.pyplot as plt

# Figure object
fig = plt.figure()

# Data: market share of companies
companies = ['Company A', 'Company B', 'Company C', 'Company D']
market_share = [35, 30, 25, 10]

# Create a pie chart
plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightgreen', 'lightcoral'])

# Customizing the plot
plt.title('Market Share of Companies')

# Adding a shadow for a 3D effect
plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue', 'lightgreen', 'lightcoral'], shadow=True)

# Save the plot
plt.plot()
fig.savefig('plots/pie.png')

