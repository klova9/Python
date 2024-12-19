import unittest
from solver import find_next_empty, is_valid, solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def setUp(self):
        self.board = [
            [5, 3, -1, -1, 7, -1, -1, -1, -1],
            [6, -1, -1, 1, 9, 5, -1, -1, -1],
            [-1, 9, 8, -1, -1, -1, -1, 6, -1],
            [8, -1, -1, -1, 6, -1, -1, -1, 3],
            [4, -1, -1, 8, -1, 3, -1, -1, 1],
            [7, -1, -1, -1, 2, -1, -1, -1, 6],
            [-1, 6, -1, -1, -1, -1, 2, 8, -1],
            [-1, -1, -1, 4, 1, 9, -1, -1, 5],
            [-1, -1, -1, -1, 8, -1, -1, 7, 9]
        ]

    def test_find_next_empty(self):
        row, col = find_next_empty(self.board)
        self.assertEqual((row, col), (0, 2))

    def test_is_valid(self):
        self.assertTrue(is_valid(self.board, 1, 0, 2))
        self.assertFalse(is_valid(self.board, 5, 0, 2))

    def test_solve_sudoku(self):
        self.assertTrue(solve_sudoku(self.board))
        self.assertEqual(self.board, [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ])

if __name__ == '__main__':
    unittest.main()