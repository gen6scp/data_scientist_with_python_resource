## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_031_exploring_text_vectors_part_2 import filtered_tfidf, articles

sys.stdout = org_stdout


from sklearn.model_selection import train_test_split

# Split data
y = articles['category']
X_train, X_test, y_train, y_test = train_test_split(filtered_tfidf.toarray(), y, stratify=y, random_state=42)

# Train Naive Bayes classifier
from sklearn.naive_bayes import MultinomialNB
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Model accuracy
print("* Naive Bayes Model Accuracy")
print(nb.score(X_test, y_test))
