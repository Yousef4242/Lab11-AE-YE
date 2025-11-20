# https://github.com/Yousef4242/Lab11-AE-YE.git
# Partner 1: Yousef El-Dakkak
# Partner 2: Aiden E


import unittest
from calculator import mul, div, logarithm, hypotenuse, square_root


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        # basic positive numbers
        self.assertEqual(mul(3, 4), 12)
        # negative and zero cases
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self):
        # normal division
        self.assertAlmostEqual(div(10, 4), 2.5)
        self.assertAlmostEqual(div(-9, 3), -3.0)
        # division by zero should raise ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log_invalid_argument(self):
        # base <= 0
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)

        # base == 1
        with self.assertRaises(ValueError):
            logarithm(1, 10)

        # argument <= 0
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        # classic 3-4-5 triangle
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        # symmetric case
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        # perfect square
        self.assertAlmostEqual(square_root(16), 4.0)
        # non-perfect square
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
        # negative should raise ValueError
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()
