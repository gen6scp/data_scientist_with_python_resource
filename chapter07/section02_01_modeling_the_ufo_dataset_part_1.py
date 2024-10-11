## INCLUDE PY FILES
import sys, io, os
org_stdout = sys.stdout
sys.stdout = io.StringIO()

from section01_07_selecting_the_ideal_dataset import ufo, ufo_dropped, pd, np, desc_tfidf, vectorizer

sys.stdout = org_stdout


from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Define words_to_filter
def words_to_filter(feature_names, tfidf_matrix, threshold):
    """
    Filter words based on a given threshold.
    
    Parameters:
    - feature_names (array-like): List of feature names (words).
    - tfidf_matrix (array-like): The TF-IDF matrix.
    - threshold (int): The threshold for filtering words.
    
    Returns:
    - filtered_words (list): List of words that meet the filtering criteria.
    """
    # Calculate the sum of TF-IDF scores for each word across all documents
    word_scores = np.sum(tfidf_matrix, axis=0)
    
    # Filter words that have a sum greater than or equal to the threshold
    filtered_words = [feature_names[i] for i in range(len(feature_names)) if word_scores[0, i] >= threshold]
    
    return filtered_words


# Filter TF-IDF vectors
filtered_words = words_to_filter(vectorizer.get_feature_names(), desc_tfidf, 4)
filtered_tfidf = desc_tfidf[:, [vectorizer.vocabulary_[word] for word in filtered_words]]

# Labels
y = ufo_dropped['month']

# Split data
X_train, X_test, y_train, y_test = train_test_split(filtered_tfidf.toarray(), y, stratify=y, random_state=42)

# Train Naive Bayes classifier
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Model accuracy
print("* Naive Bayes Model Accuracy")
print(nb.score(X_test, y_test))
