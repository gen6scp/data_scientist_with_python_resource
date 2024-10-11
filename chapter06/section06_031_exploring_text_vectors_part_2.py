## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_030_exploring_text_vectors_part_1 import X, features, top_tfidf_features, articles

sys.stdout = org_stdout


def filter_top_words(tfidf_matrix, features, top_n=5):
    top_words = set()
    for row in tfidf_matrix:
        top_words.update(top_tfidf_features(row.toarray().flatten(), features, top_n).keys())
    return top_words

# Example usage
top_words = filter_top_words(X, features)
filtered_tfidf = X[:, [features.index(word) for word in top_words]]

print(filtered_tfidf.toarray())
