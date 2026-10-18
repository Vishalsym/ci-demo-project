import unittest
from utils import square, is_even, cube


class TestUtils(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(7), 50)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_is_even_true(self):
        self.assertTrue(is_even(10))

    def test_is_even_false(self):
        self.assertFalse(is_even(7))

    def test_cube(self):
        self.assertEqual(cube(3), 27)


if __name__ == "__main__":
    unittest.main()
