import unittest
from matrix import Matrix
from algos import *
import numpy as np

class TestAlgos(unittest.TestCase):

    def test_maxmin_and_minmax(self):
        matrix = Matrix.input_from_file("resources\\test_1.txt")
        self.assertEqual(maximin(matr=matrix,param=0),8)
        self.assertEqual(minimax(matr=matrix,param=0),5)
        self.assertEqual(maximin(matr=matrix,param=1),4)
        self.assertEqual(minimax(matr=matrix,param=1),7)

    def test_dominant(self):
        matrix = Matrix.input_from_file("resources\\test_2.txt")
        rs_matrix_0 = Matrix.input_from_file("resources\\rs_test2_0.txt")
        self.assertTrue(np.array_equal(rs_matrix_0.matrix,dominant(matr=matrix,param=0).matrix))
        self.assertTrue(np.array_equal(rs_matrix_0.matrix,weaklyDominant(matr=matrix,param=0).matrix))
        rs_matrix_1 = Matrix.input_from_file("resources\\rs_test2_1.txt")
        self.assertTrue(np.array_equal(rs_matrix_1.matrix,dominant(matr=matrix,param=1).matrix))
        self.assertTrue(np.array_equal(rs_matrix_1.matrix,weaklyDominant(matr=matrix,param=1).matrix))

    def test_nesh(self):
        matrix = Matrix.input_from_file("resources\\test_3.txt")
        self.assertEqual(nesh(matr=matrix),(0,0))


if __name__ == '__main__':
    # unittest.main()
    _matrix = Matrix.input_from_file("resources\\test_2.txt")
    rs_matrix = dominant(_matrix, 0)
    print(_matrix)
    print(rs_matrix)
