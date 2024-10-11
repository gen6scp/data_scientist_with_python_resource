# text_analysis.py (updated with documentation)

def count_words(filepath, words_list):
    """Count occurrences of words in a text file.

    Parameters:
    -----------
    filepath : str
        The path to the text file.
    words_list : list
        A list of words to search for in the text.

    Returns:
    --------
    int
        The number of times the words in the list appear in the text.
    """
    with open(filepath, 'r') as file:
        text = file.read().lower()

    count = sum(word in text for word in words_list)
    return count
