import numpy as np


def leading_minor(m, k):
    m = np.delete(m, k, 0)
    m = np.delete(m, k, 1)
    return m


def lu(matrix):
    """Rozkład macierzy bez wyboru częściowego elementu głównego (Macierzy permutacji)"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("Podana wartość nie jest macierzą")
    if matrix.ndim == 0:
        raise TypeError("Macierz nie może być wymiaru 0x0")
    matrix = np.asmatrix(matrix)
    if not matrix.shape[0] == matrix.shape[1]:
        return False
    if np.linalg.det(matrix) != 0:
        for _ in range(1, matrix.shape[0]):
            matrix = leading_minor(matrix, -1)
            if np.linalg.det(matrix) == 0:
                return False
        else:
            return True
    return False
