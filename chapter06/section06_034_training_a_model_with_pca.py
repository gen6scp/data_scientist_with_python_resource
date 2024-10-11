## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_033_using_pca import X_pca, articles

sys.stdout = org_stdout


from sklearn.model_selection import train_test_split

# Split data
y = articles['category']
X_train, X_test, y_train, y_test = train_test_split(X_pca, y, stratify=y, random_state=42)

# Train KNN model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Model accuracy
print("* KNN Model Accuracy")
print(knn.score(X_test, y_test))
