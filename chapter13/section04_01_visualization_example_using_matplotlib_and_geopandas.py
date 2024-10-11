## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section3_04_sql_queries_for_data_analysis_using_python import df_locations

sys.stdout = org_stdout


import matplotlib.pyplot as plt
import geopandas as gpd

# Assuming df has 'Latitude' and 'Longitude' columns
gdf = gpd.GeoDataFrame(df_locations, geometry=gpd.points_from_xy(df_locations.lng, df_locations.lat))

# Load world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot incidents on a world map
ax = world.plot(figsize=(10, 10))

# Set the xlim and ylim to zoom in on Europe
# These limits are approximate and can be adjusted for better zoom
ax.set_xlim([20, 45])  # Longitude range covering Europe
ax.set_ylim([40, 60])   # Latitude range covering Europe

# Set Mark and Title
gdf.plot(ax=ax, color='red', marker='o', markersize=5)
plt.title('Geolocated Incidents of Russia-Ukraine War')

# Save the map plot to a file
fig = ax.get_figure()
fig.savefig('plots/geolocated_incidents.png')

