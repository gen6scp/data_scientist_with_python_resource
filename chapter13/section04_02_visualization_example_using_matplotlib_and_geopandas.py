import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


# Reconnect to the SQLite database to perform SQL queries
conn = sqlite3.connect('osint_data.db')
# Query: Count incidents by date
query = '''SELECT date, COUNT(*) AS incident_count
            FROM articles
            GROUP BY date
            ORDER BY date DESC;'''
df = pd.read_sql_query(query, conn)

# Ensure 'Date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract day of year to track trends over time
df['day_of_year'] = df['date'].dt.dayofyear

# Example of linear regression: incidents over the course of the year
slope, intercept, r_value, p_value, std_err = linregress(df['day_of_year'], df['incident_count'])

print(f"Slope: {slope}, R-squared: {r_value**2}")

# Plot the trend
plt.plot(df['day_of_year'], df['incident_count'], 'o', label='Data Points')
plt.plot(df['day_of_year'], intercept + slope * df['day_of_year'], 'r', label='Fitted Line')
plt.legend()
plt.xlabel('Day of Year')
plt.ylabel('Incident Count')
plt.title('Incident Trend Over Time')

# Save the trend plot to a file
plt.savefig('plots/incident_trend_over_time.png')
