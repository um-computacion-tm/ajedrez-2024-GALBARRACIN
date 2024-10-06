import unittest
from pieces.rook import Rook
from pieces.piece import Piece


class TestRook(unittest.TestCase):


    # ===== Configuración básica con un tablero vacío =====
    def setUp(self):
        self.__empty_board__ = [[None for _ in range(8)] for _ in range(8)]
        self.__rook_white__ = Rook('white')
        self.__rook_black__ = Rook('black')


    # ===== Movimiento horizontal válido =====
    def test_valid_move_horizontal(self):
        self.assertTrue(self.__rook_white__.is_valid_move(0, 0, 0, 5, self.__empty_board__))
        self.assertTrue(self.__rook_black__.is_valid_move(7, 7, 7, 0, self.__empty_board__))


    # ===== Movimiento vertical válido =====
    def test_valid_move_vertical(self):
        self.assertTrue(self.__rook_white__.is_valid_move(0, 0, 5, 0, self.__empty_board__))
        self.assertTrue(self.__rook_black__.is_valid_move(7, 7, 0, 7, self.__empty_board__))


    # ===== Movimiento diagonal no válido =====
    def test_invalid_move_diagonal(self):
        self.assertFalse(self.__rook_white__.is_valid_move(0, 0, 5, 5, self.__empty_board__))
        self.assertFalse(self.__rook_black__.is_valid_move(7, 7, 2, 2, self.__empty_board__))


    # ===== Movimiento con un obstáculo en el camino horizontal =====
    def test_invalid_move_with_obstacle_horizontal(self):
        self.__empty_board__[0][3] = Piece('black')  # Colocamos un obstáculo en la posición (0, 3)
        self.assertFalse(self.__rook_white__.is_valid_move(0, 0, 0, 5, self.__empty_board__))


    # ===== Movimiento con un obstáculo en el camino vertical =====
    def test_invalid_move_with_obstacle_vertical(self):
        self.__empty_board__[3][0] = Piece('white')  # Colocamos un obstáculo en la posición (3, 0)
        self.assertFalse(self.__rook_black__.is_valid_move(0, 0, 5, 0, self.__empty_board__))


    # ===== Movimiento válido de captura =====
    def test_capture_move(self):
        self.__empty_board__[0][5] = Piece('black')  # Colocamos una pieza para capturar
        self.assertTrue(self.__rook_white__.is_valid_move(0, 0, 0, 5, self.__empty_board__))

if __name__ == '__main__':
    unittest.main()