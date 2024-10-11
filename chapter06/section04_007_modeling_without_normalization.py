from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Load dataset
wine = load_wine()
X = wine.data
y = wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# KNN model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Model accuracy
print("* KNN Model Accuracy")
print(knn.score(X_test, y_test))
