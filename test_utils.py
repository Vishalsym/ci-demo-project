import unittest
from utils import square, is_even


class TestUtils(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(7), 49)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_is_even_true(self):
        self.assertTrue(is_even(10))

    def test_is_even_false(self):
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()
