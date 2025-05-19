import unittest
from utils.string_parser import string_parser

class String_Parser_Test(unittest.TestCase):
    def test_words_are_split(self):
        self.assertEqual(string_parser("banana,apple,mango"), ["banana", "apple", "mango"])
