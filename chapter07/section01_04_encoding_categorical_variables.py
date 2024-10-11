## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_03_identifying_features_for_standardization import ufo, ufo_dropped, pd, np

sys.stdout = org_stdout


# Binary encode 'country' column
ufo_dropped['country_enc'] = ufo_dropped['country'].apply(lambda x: 1 if x == 'us' else 0)

# One-hot encode 'shape' column
type_dummies = pd.get_dummies(ufo_dropped['shape'])
ufo_dropped = pd.concat([ufo_dropped, type_dummies], axis=1)

# Print
print(ufo_dropped.info())

# Convert 'latitude' to a proper type (float64 as well as longitude type)
ufo_dropped['latitude'] = ufo_dropped['latitude'].astype('float64')

# Check some columns
print("\n* Check some columns")
print(ufo_dropped[['datetime', 'seconds_log', 'country_enc', 'shape', 'latitude', 'round', 'light']].head())



# Keep checking the data. Plot a world map
import matplotlib.pyplot as plt
import geopandas as gpd

# Assuming df has 'Latitude' and 'Longitude' columns
location = ufo_dropped[['longitude', 'latitude']]
gdf = gpd.GeoDataFrame(location, geometry=gpd.points_from_xy(location.longitude, location.latitude))

# Load world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot incidents on a world map
ax = world.plot(figsize=(10, 5))

# Set the xlim and ylim to zoom in on Europe
# These limits are approximate and can be adjusted for better zoom
ax.set_xlim([-180, 180])  # Longitude range covering World
ax.set_ylim([-90, 90])   # Latitude range covering World

# Set Mark and Title
gdf.plot(ax=ax, color='red', marker='o', markersize=5)
plt.title('Geolocated UFO Incidents')

# Save the map plot to a file
fig = ax.get_figure()
fig.savefig('plots/geolocated_incidents.png')
