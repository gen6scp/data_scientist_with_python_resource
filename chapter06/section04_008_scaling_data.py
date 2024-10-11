from sklearn.neighbors import KNeighborsClassifier
from sklearn . datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler


# Select columns to scale
wine = load_wine()
wine_subset = wine.data[:, [2, 3, 4]]
print("* Before Scaling")
print(np.var(wine_subset[:,[1]]))

# Standardize
scaler = StandardScaler()
wine_subset_scaled = scaler.fit_transform(wine_subset)
print("* After Scaling")
print(np.var(wine_subset_scaled[:,[1]]))

# Set the scaled values
wine.data[:, [2, 3, 4]] = wine_subset_scaled

# Check KNN accuracy
X = wine.data
y = wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# KNN model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Model accuracy
print("* KNN Model Accuracy (After Scaling)")
print(knn.score(X_test, y_test))
