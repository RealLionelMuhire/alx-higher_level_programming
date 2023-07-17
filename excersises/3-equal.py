#!/usr/bin/python3
import unittest
def is_2lists(list1, list2):
    return list1 == list2


class Test_lists(unittest.TestCase):
    def test_is_2lists_equal(self):
        list1 = [1, 2, 4]
        list2 = [1, 2, 4]
        self.assertTrue(is_2lists(list1, list2))
    
    def test_is_not_equal(self):
        self.assertFalse(is_2lists(list1=[1, 2, 3], list2=[2, 3, 4]))

unittest.main()