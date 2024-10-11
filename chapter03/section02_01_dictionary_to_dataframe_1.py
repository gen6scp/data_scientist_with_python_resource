# Define city names, population, and temperature data
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
population = [8419600, 3980400, 2716000, 2328000, 1690000]
temperature = [13.3, 18.5, 10.2, 20.6, 22.4]

# Import pandas as pd
import pandas as pd

# Create a dictionary from the lists
city_data = {
    'City': cities,
    'Population': population,
    'Temperature (°C)': temperature
}

# Create a DataFrame from the dictionary
city_df = pd.DataFrame(city_data)

# Print the DataFrame
print(city_df)
