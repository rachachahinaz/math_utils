import unittest
from math_utils import multiply

class TestMathUtils(unittest.TestCase):
      def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

      def test_multiply_negative(self):
        self.assertEqual(multiply(-1, 5), -5)

      def test_multiply_zero(self):
        self.assertEqual(multiply(0, 10), 0)

      if __name__ == "__main__":
         unittest.main()