import unittest
from math_utils import add

class TestSumFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(3,5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-3,-4), -7)
        
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add(-3,10), 7)

if __name__ == "__main__":
    unittest.main()
