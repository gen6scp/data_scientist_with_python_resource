# text_analysis.py

def count_words(filepath, words_list):
    """
    Count occurrences of words in a text file. This returns the total count of the specified words.
    """
    with open(filepath, 'r') as file:
        text = file.read().lower()

    count = sum(word in text for word in words_list)
    print(f"The words {words_list} appear {count} times in the text.")
    return count
