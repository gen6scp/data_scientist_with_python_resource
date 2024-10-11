## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_031_exploring_text_vectors_part_2 import filtered_tfidf, articles

sys.stdout = org_stdout


from sklearn.decomposition import PCA

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(filtered_tfidf.toarray())

# Explained variance
print(pca.explained_variance_ratio_)

