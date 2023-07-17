#!/usr/bin/python3
import unittest

class TestFloatComput(unittest.TestCase):
    def test_check_add(self):
        result = 0.999 + 0.001
        self.assertAlmostEqual(result, 1.0000, places=4)
    
    def test_check_mul(self):
        result = 0.4 * 0.003
        self.assertAlmostEqual(result, 0.0012, places=4)
    
    def test_check_div(self):
        result = 22 / 7
        from math import pi
        self.assertAlmostEqual(result, pi, places=2)

if __name__ == "__main__":
    unittest.main()
