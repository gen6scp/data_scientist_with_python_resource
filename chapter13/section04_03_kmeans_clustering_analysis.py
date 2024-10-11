import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Reconnect to the SQLite database to perform SQL queries
conn = sqlite3.connect('osint_data.db')

# Example Query 1: Count incidents by location
query1 = '''SELECT lat, lng, COUNT(*) AS incident_count
            FROM articles
            GROUP BY lat, lng
            ORDER BY incident_count DESC;'''
df_locations = pd.read_sql_query(query1, conn)

# Prepare the data for clustering
X = df_locations[['lat', 'lng']].values

# Apply K-Means clustering
kmeans = KMeans(n_clusters=10)
df_locations['Cluster'] = kmeans.fit_predict(X)

# Visualize the clusters on a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_locations['lng'], df_locations['lat'], c=df_locations['Cluster'], cmap='viridis', marker='o')
plt.title('K-Means Clustering of Incident Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Save the clustering plot to a file
plt.savefig('plots/kmeans_clustering_incidents.png')

# Provide insights
cluster_centers = kmeans.cluster_centers_
print(f"Cluster Centers (Hotspots):\n {cluster_centers}")
