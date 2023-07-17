#!/usr/bin/python3
import unittest


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in primes:
            self.assertTrue(is_prime(prime), "{}is prime".format(prime))
        
    def test_non_prime(self):
        n_pri = [4, 8, 12, 15, 21, 33]
        for num in n_pri:
            self.assertFalse(is_prime(num), f"{num} is not prime")
    
    def test_negative(self):
        neg_n = [-2, -11, -22, -24]
        for num in neg_n:
            self.assertFalse(is_prime(num), f"{num} is negative")
    
    def test_zero_one(self):
        zerOne = [0, 1]
        for num in zerOne:
            self.assertFalse(is_prime(num), f"{num} is zero or one")


if __name__ == "__main__":
    unittest.main()