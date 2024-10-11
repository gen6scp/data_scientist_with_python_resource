## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section3_005_class_imbalance import feedback

sys.stdout = org_stdout


# Import Sklearn for correcting class distribution
from sklearn.model_selection import train_test_split

# Features and labels
X = feedback.drop(columns=['feedback'])
y = feedback['feedback']

# Stratified sampling
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

print("* Test")
print(y_test.value_counts())
print("* Train")
print(y_train.value_counts())
