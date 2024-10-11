import numpy as np

# Generate a simulated temperature dataset (365 days)
np.random.seed(42)
temperatures = np.random.normal(loc=15, scale=10, size=365)  # Mean 15°C, SD 10°C

# Calculate the moving average (window size of 7 days)
moving_avg = np.convolve(temperatures, np.ones(7)/7, mode='valid')

# Detect temperature anomalies (values more than 2 standard deviations away from the mean)
mean_temp = np.mean(temperatures)
std_temp = np.std(temperatures)
anomalies = temperatures[np.abs(temperatures - mean_temp) > 2 * std_temp]

print(f"Mean Temperature: {mean_temp:.2f}°C")
print(f"Detected Anomalies: {anomalies}")

