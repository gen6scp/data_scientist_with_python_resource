import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data
data = {
    'article_id': [1, 2, 3],
    'title': ['Machine Learning Basics', 'Introduction to Data Science', 'Deep Learning Techniques']
}
articles = pd.DataFrame(data)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
title_tfidf = vectorizer.fit_transform(articles['title'])

print(title_tfidf.toarray())
