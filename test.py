import unittest
from my_sum import sum
from fractions import Fraction

class TestSum(unittest.TestCase):

    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            sum(data)

if __name__ == '__main__':
    unittest.main()
