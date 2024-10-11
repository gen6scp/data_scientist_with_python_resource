## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_07_selecting_the_ideal_dataset import ufo, ufo_dropped, pd, np

sys.stdout = org_stdout


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Features and labels
X = ufo_dropped.drop(columns=['country_enc'])
y = ufo_dropped['country_enc']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

# Train KNN model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Model accuracy
print("* KNN Model Accuracy")
print(knn.score(X_test, y_test))
