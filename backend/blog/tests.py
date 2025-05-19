from django.test import TestCase
from utils.string_parser import string_parser
from math_utils import add

# Create your tests here.
class TestSumFunction(TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3,5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3,-4), -7)
        
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add(-3,10), 7)


class StringParserTest(TestCase):
    def test_words_are_split(self):
        self.assertEqual(string_parser("banana,apple,mango"), ["banana", "apple", "mango"])

    def test_words_with_spaces(self):
        self.assertEqual(string_parser("   banana   ,  apple  ,mango"), ["banana", "apple", "mango"])
