# tests/test_text_analysis.py

import unittest
from text_analysis import count_words

class TestTextAnalysis(unittest.TestCase):

    def test_count_words(self):
        result = count_words('tests/sample.txt', ['python', 'data'])
        self.assertEqual(result, 2)  # assuming 'python' and 'data' appear 2 times

if __name__ == '__main__':
    unittest.main()
