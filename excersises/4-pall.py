#!/usr/bin/python3
import unittest

    
def is_pall(string):
    return string == string[::-1]


class Test_isPall(unittest.TestCase):
    def test_is_pall(self):
        string = "madam"
        print(f"Testing if <{string}> i pallindrome")
        self.assertTrue(is_pall(string), f"{string} is pallindrome")

    def test_is_not_pall(self):
        string = "ALX is powerfull oportunitity"
        print(f"Testing if <{string}> i pallindrome")
        self.assertFalse(is_pall(string), f"{string} is not pallndrome")
    
    def test_empty_1char(self):
        string = ""
        print(f"testing <{string}> is pallindrome")
        self.assertTrue(is_pall(string), f"{string} is pallindrome")


if __name__ == "__main__":
    unittest.main()