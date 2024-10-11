import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data
data = {
    'article_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'title': [
        'Machine Learning Basics',
        'Introduction to Data Science',
        'Deep Learning Techniques',
        'Data Analysis with Python',
        'Statistics for Machine Learning',
        'Advanced Data Visualization',
        'Natural Language Processing',
        'Big Data Technologies',
        'Reinforcement Learning Concepts',
        'Computer Vision Applications'
    ],
    
    'category': ['ML', 'DS', 'DL', 'DS', 'ML', 'DS', 'ML', 'ML', 'ML', 'ML'],
    'pages': [312, 123, 210, 220, 290, 159, 270, 143, 396, 233],
    'points': [0.8, 0.5, 0.3, 0.2, 0.7, 0.3, 0.6, 0.5, 0.9, 0.8]
}

articles = pd.DataFrame(data)

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(articles['title'])

# Labels
y = articles['category']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=42)

# Train Naive Bayes classifier
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Model accuracy
print("* Naive Bayes Accuracy")
print(nb.score(X_test, y_test))
