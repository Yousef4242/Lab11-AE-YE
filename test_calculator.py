# https://github.com/Yousef4242/Lab11-AE-YE.git
# Partner 1: Yousef El-Dakkak
# Partner 2: Aiden E


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 4), 9)
        self.assertEqual(add(5, -4), 1)
        self.assertEqual(add(-5, -4), -9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 4), 1)
        self.assertEqual(subtract(5, -4), 9)
        self.assertEqual(subtract(-5, -4), -1)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(10, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 1)


    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, -5)

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(0, 10), 0)
        self.assertEqual(mul(-10, 10), -100)

    def test_divide(self): # 3 assertions  fill in code
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-50, 5), -10)
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))


if __name__ == "__main__":
    unittest.main()