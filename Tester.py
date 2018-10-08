import unittest
import random

from BinarySearch import BinarySearch
class SearchCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def testBinarySearchChecker(self):
        """Fail to Find Designated Number - your Algorithm is wrong"""
        array = [7,10,20,21,23,29,30,56,32]
        self.assertEqual(BinarySearch(array,random.choice(array)),True)

if __name__ == '__main__':
    unittest.main()