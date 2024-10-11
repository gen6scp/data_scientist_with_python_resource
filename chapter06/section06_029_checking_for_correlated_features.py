## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section6_027_identifying_areas_for_feature_selection import articles

sys.stdout = org_stdout


# Drop 'article_id' column
articles_reduced = articles.drop(columns=['article_id'])

# Calculate correlations
correlations = articles_reduced.corr()

print(correlations)
