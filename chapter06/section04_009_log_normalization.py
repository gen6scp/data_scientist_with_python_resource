from sklearn.neighbors import KNeighborsClassifier
from sklearn . datasets import load_wine
from sklearn.model_selection import train_test_split
import numpy as np


# Print variance of 'Proline' column
wine = load_wine()
print("* Before Log Normalization")
print(wine.data[:, 12].var())

# Log normalization
wine.data[:, 12] = np.log(wine.data[:, 12])

# Check variance again
print("* After Log Normalization")
print(wine.data[:, 12].var())


# Check KNN accuracy
X = wine.data
y = wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# KNN model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Model accuracy
print("* KNN Model Accuracy (After Log Normalization)")
print(knn.score(X_test, y_test))
