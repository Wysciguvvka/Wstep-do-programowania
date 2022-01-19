import unittest
import numpy as np
import scipy.linalg


class TestLU(unittest.TestCase):

    def test_pure_lu(self):
        matrix = np.array([[5, 1],
                           [1, 1]])
        p, l, u = scipy.linalg.lu(matrix)
        self.assertIs(np.array_equal(matrix, np.matmul(l, u)), True)
        matrix = np.array([[0, 1, 2],
                           [3, 4, 1],
                           [0, 1, 8]])
        l, u = scipy.linalg.lu_factor(matrix)
        self.assertIs(np.array_equal(matrix, np.matmul(l, u)), False)

    def test_zero_det(self):
        matrix = np.array([[1, 1],
                           [1, 1]])
        self.assertEqual(np.linalg.det(matrix), 0)

    def test_is_square(self):
        matrix = np.array([[0, 1],
                           [1, 1]])
        self.assertEqual(matrix.shape[0], matrix.shape[1])

    def test_non_square(self):
        matrix = np.array([[0, 1], [0, 1],
                           [1, 1]])
        with self.assertRaises(ValueError):
            l, u = scipy.linalg.lu_factor(matrix)


if __name__ == '__main__':
    unittest.main()
