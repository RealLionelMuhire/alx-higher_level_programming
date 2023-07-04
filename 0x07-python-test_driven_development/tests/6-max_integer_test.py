import unittest
from max_integer import max_integer

class MaxIntegerTestCase(unittest.TestCase):
    def test_empty_list(self):
        # Test case for an empty list
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        # Test case for a list of positive numbers
        result = max_integer([1, 3, 2, 5, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        # Test case for a list of negative numbers
        result = max_integer([-1, -3, -2, -5, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        # Test case for a list of mixed positive and negative numbers
        result = max_integer([-1, 3, -2, 5, -4])
        self.assertEqual(result, 5)

    def test_duplicate_numbers(self):
        # Test case for a list with duplicate numbers
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_single_number(self):
        # Test case for a list with a single number
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_empty_string(self):
        # Test case for an empty string
        result = max_integer("")
        self.assertIsNone(result)

    def test_invalid_input(self):
        # Test case for an invalid input (non-numeric elements in the list)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4, 5])

if __name__ == '__main__':
    unittest.main()
