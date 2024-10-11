## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_05_features_from_dates import ufo, ufo_dropped, pd, np

sys.stdout = org_stdout


from sklearn.feature_extraction.text import TfidfVectorizer

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
desc_tfidf = vectorizer.fit_transform(ufo_dropped['comments'])

print("* Dimension of the TF-IDF Descriptor")
print(desc_tfidf.shape)
