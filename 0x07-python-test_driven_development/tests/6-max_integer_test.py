import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxinteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_integers(self):
        self.assertEqual(max_integer([1, 2, 4, 6]), 6)

    def test_floats(self):
        self.assertEqual(max_integer([1.4, 1.5, 3.5]), 3.5)

    def test_non_integers(self):
        pass

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 4, 6.5, 9.5]), 9.5)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-2, 4, -9, 33]), 33)
