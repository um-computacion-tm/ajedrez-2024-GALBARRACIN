import unittest
from pieces.rook import Rook
from pieces.piece import Piece


class TestRook(unittest.TestCase):


    # ===== Configuración básica con un tablero vacío =====
    def setUp(self):
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        self.rook_white = Rook('white')
        self.rook_black = Rook('black')


    # ===== Movimiento horizontal válido =====
    def test_valid_move_horizontal(self):
        self.assertTrue(self.rook_white.is_valid_move(0, 0, 0, 5, self.empty_board))
        self.assertTrue(self.rook_black.is_valid_move(7, 7, 7, 0, self.empty_board))


    # ===== Movimiento vertical válido =====
    def test_valid_move_vertical(self):
        self.assertTrue(self.rook_white.is_valid_move(0, 0, 5, 0, self.empty_board))
        self.assertTrue(self.rook_black.is_valid_move(7, 7, 0, 7, self.empty_board))


    # ===== Movimiento diagonal no válido =====
    def test_invalid_move_diagonal(self):
        self.assertFalse(self.rook_white.is_valid_move(0, 0, 5, 5, self.empty_board))
        self.assertFalse(self.rook_black.is_valid_move(7, 7, 2, 2, self.empty_board))


    # ===== Movimiento con un obstáculo en el camino horizontal =====
    def test_invalid_move_with_obstacle_horizontal(self):
        self.empty_board[0][3] = Piece('black')  # Colocamos un obstáculo en la posición (0, 3)
        self.assertFalse(self.rook_white.is_valid_move(0, 0, 0, 5, self.empty_board))


    # ===== Movimiento con un obstáculo en el camino vertical =====
    def test_invalid_move_with_obstacle_vertical(self):
        self.empty_board[3][0] = Piece('white')  # Colocamos un obstáculo en la posición (3, 0)
        self.assertFalse(self.rook_black.is_valid_move(0, 0, 5, 0, self.empty_board))


    # ===== Movimiento válido de captura =====
    def test_capture_move(self):
        self.empty_board[0][5] = Piece('black')  # Colocamos una pieza para capturar
        self.assertTrue(self.rook_white.is_valid_move(0, 0, 0, 5, self.empty_board))

if __name__ == '__main__':
    unittest.main()