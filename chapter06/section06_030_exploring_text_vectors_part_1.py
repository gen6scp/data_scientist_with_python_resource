## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_027_identifying_areas_for_feature_selection import articles

sys.stdout = org_stdout



import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(articles['title'])

def top_tfidf_features(row, features, top_n=5):
    top_ids = np.argsort(row)[::-1][:top_n]
    top_features = [features[i] for i in top_ids]
    top_scores = row[top_ids]
    return {top_features[i]: top_scores[i] for i in range(top_n)}

# Example usage
row = X[0].toarray().flatten()
features = vectorizer.get_feature_names()
print(top_tfidf_features(row, features))
