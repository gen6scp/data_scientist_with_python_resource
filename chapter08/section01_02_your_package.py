# customer_reviews.py

from text_analysis import count_words

# Analyze customer reviews
positive_count = count_words('reviews.txt', ['excellent', 'fantastic', 'amazing'])
negative_count = count_words('reviews.txt', ['poor', 'terrible', 'bad'])

print(f"Positive words: {positive_count}")
print(f"Negative words: {negative_count}")
