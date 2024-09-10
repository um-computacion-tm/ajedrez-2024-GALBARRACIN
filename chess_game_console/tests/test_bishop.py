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


    # ===== Movimiento válido en diagonal ===== 
    def test_valid_move_diagonal_no_obstacles(self):
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 5, 3, self.empty_board))  # Diagonal hacia adelante
        self.assertTrue(self.white_bishop.is_valid_move(5, 3, 2, 0, self.empty_board))  # Diagonal hacia atrás


    # =====  Movimiento inválido (no diagonal) =====
    def test_invalid_move_not_diagonal(self): 
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 3, 0, self.empty_board))  # Movimiento vertical
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 2, 2, self.empty_board))  # Movimiento horizontal


    # =====  Movimiento fuera del tablero ===== 
    def test_invalid_move_out_of_bounds(self):
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 9, 7, self.empty_board))  # Fuera de los límites


    # =====  Colocar una pieza en el camino =====
    def test_valid_move_diagonal_with_obstacles(self): 
        self.empty_board[3][1] = self.black_bishop  # Poner un alfil en el camino
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Diagonal con obstáculo


    # =====  Movimiento válido para capturar ===== 
    def test_valid_move_capture(self):
        self.empty_board[4][2] = self.black_bishop  # Colocar una pieza enemiga en la posición de destino
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Movimiento para capturar

if __name__ == '__main__':
    unittest.main()
