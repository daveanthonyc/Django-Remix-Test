import unittest
from utils.string_parser import string_parser

class StringParserTest(unittest.TestCase):
    def test_words_are_split(self):
        self.assertEqual(string_parser("banana,apple,mango"), ["banana", "apple", "mango"])

    def test_words_with_spaces(self):
        self.assertEqual(string_parser("   banana   ,  apple  ,mango"), ["banana", "apple", "mango"])
