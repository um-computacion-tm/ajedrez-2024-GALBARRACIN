# tests/test_bishop.py

import unittest
from pieces.bishop import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.white_bishop = Bishop('white')
        self.black_bishop = Bishop('black')
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_symbol(self):
        self.assertEqual(self.white_bishop.symbol(), 'B')
        self.assertEqual(self.black_bishop.symbol(), 'b')

    def test_valid_move_diagonal_no_obstacles(self):
        # Movimiento válido en diagonal
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 5, 3, self.empty_board))  # Diagonal hacia adelante
        self.assertTrue(self.white_bishop.is_valid_move(5, 3, 2, 0, self.empty_board))  # Diagonal hacia atrás

    def test_invalid_move_not_diagonal(self):
        # Movimiento inválido (no diagonal)
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 3, 0, self.empty_board))  # Movimiento vertical
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 2, 2, self.empty_board))  # Movimiento horizontal

    def test_invalid_move_out_of_bounds(self):
        # Movimiento fuera del tablero
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 9, 7, self.empty_board))  # Fuera de los límites

    def test_valid_move_diagonal_with_obstacles(self):
        # Colocar una pieza en el camino
        self.empty_board[3][1] = self.black_bishop  # Poner un alfil en el camino
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Diagonal con obstáculo

    def test_valid_move_capture(self):
        # Movimiento válido para capturar
        self.empty_board[4][2] = self.black_bishop  # Colocar una pieza enemiga en la posición de destino
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Movimiento para capturar

if __name__ == '__main__':
    unittest.main()
