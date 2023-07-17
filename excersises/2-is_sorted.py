#!/usr/bin/python3
import unittest


def is_sorted(list):
    return list == sorted(list)

class Test_list(unittest.TestCase):
    def test_is_sorted(self):
        list = [1, 2, 5, 79, 91]
        self.assertTrue(is_sorted(list), f"Is sorted")
    
    def test_is_not_sorted(self):
        list = [1, 4, 55, 2, 6]
        self.assertFalse(is_sorted(list), "Nort sorted")
    
    def test_is_empty(self):
        list = []
        self.assertTrue(is_sorted(list), "Empty and is sorted")
    
    def test_is_onelement(self):
        list = [1]
        self.assertTrue(is_sorted(list), "! element and is sorted")

unittest.main()

