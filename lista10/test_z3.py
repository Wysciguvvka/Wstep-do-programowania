import unittest
import z3 as lu
import numpy as np


class TestLU(unittest.TestCase):

    def test_non_matrix(self):
        self.assertRaises(TypeError, lu.lu, "matrix")

    def test_non_square_matrix(self):
        matrix = np.array([[2, 3],
                           [4, 5],
                           [6, 7]])
        self.assertEqual(lu.lu(matrix), False)
        matrix = np.array([[2, 3, 4, 5],
                           [4, 5, 4, 5]])
        self.assertEqual(lu.lu(matrix), False)

    def test_zero_leading_minor(self):
        matrix = np.array([[0, 1],
                           [1, 1]])
        self.assertEqual(lu.lu(matrix), False)
        matrix = np.array([[0, 1, 2],
                           [3, 4, 1],
                           [0, 1, 8]])
        self.assertEqual(lu.lu(matrix), False)

    def test_non_invertible_matrix(self):
        matrix = np.array([[1, 1],
                           [1, 1]])
        self.assertEqual(lu.lu(matrix), False)
        matrix = np.array([[5, 5, 5],
                           [1, 1, 1],
                           [2, 6, 7]])
        self.assertEqual(lu.lu(matrix), False)

    def test_pure_lu(self):
        matrix = np.array([[2, 3, 4],
                           [4, 5, 6],
                           [2, 6, 7]])
        self.assertEqual(lu.lu(matrix), True)


if __name__ == '__main__':
    unittest.main()
