import pandas as pd

data = {
    'feedback_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'feedback': ['Positive', 'Negative', 'Negative', 'Neutral', 'Negative', 'Negative', 'Neutral', 'Positive', 'Positive', 'Positive']
}
feedback = pd.DataFrame(data)

# Check class distribution
print(feedback['feedback'].value_counts())
