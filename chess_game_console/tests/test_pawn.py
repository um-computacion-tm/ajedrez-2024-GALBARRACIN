# tests/test_pawn.py
import unittest
from pieces.pawn import Pawn
from pieces.piece import Piece

class TestPawn(unittest.TestCase):

    # ===== Configuración básica con un tablero vacío =====
    def setUp(self):
        self.__empty_board__ = [[None for _ in range(8)] for _ in range(8)]
        self.__pawn_white__ = Pawn('white')
        self.__pawn_black__ = Pawn('black')


    # ===== Movimiento válido hacia adelante (una casilla) =====
    def test_valid_move_forward_one(self):
        self.assertTrue(self.__pawn_white__.is_valid_move(6, 0, 5, 0, self.__empty_board__))
        self.assertTrue(self.__pawn_black__.is_valid_move(1, 0, 2, 0, self.__empty_board__))


    # ===== Movimiento válido hacia adelante (dos casillas en el primer movimiento) =====
    def test_valid_move_forward_two(self):
        self.assertTrue(self.__pawn_white__.is_valid_move(6, 0, 4, 0, self.__empty_board__))
        self.assertTrue(self.__pawn_black__.is_valid_move(1, 0, 3, 0, self.__empty_board__))


    # ===== Movimiento inválido porque está bloqueado por otra pieza =====
    def test_invalid_move_forward_blocked(self):
        self.__empty_board__[5][0] = Piece('white')
        self.assertFalse(self.__pawn_white__.is_valid_move(6, 0, 5, 0, self.__empty_board__))

        self.__empty_board__[2][0] = Piece('black')
        self.assertFalse(self.__pawn_black__.is_valid_move(1, 0, 2, 0, self.__empty_board__))


    # ===== Movimiento inválido hacia adelante (dos casillas) porque está bloqueado por otra pieza =====
    def test_invalid_move_forward_two_blocked(self):
        self.__empty_board__[4][0] = Piece('white')
        self.assertFalse(self.__pawn_white__.is_valid_move(6, 0, 4, 0, self.__empty_board__))

        self.__empty_board__[3][0] = Piece('black')
        self.assertFalse(self.__pawn_black__.is_valid_move(1, 0, 3, 0, self.__empty_board__))


    # ===== Captura válida en diagonal =====
    def test_valid_capture(self):
        self.__empty_board__[5][1] = Piece('black')
        self.assertTrue(self.__pawn_white__.is_valid_move(6, 0, 5, 1, self.__empty_board__))

        self.__empty_board__[2][1] = Piece('white')
        self.assertTrue(self.__pawn_black__.is_valid_move(1, 0, 2, 1, self.__empty_board__))


    # ===== Captura inválida porque no hay pieza en la casilla destino =====
    def test_invalid_capture_empty(self):
        self.assertFalse(self.__pawn_white__.is_valid_move(6, 0, 5, 1, self.__empty_board__))
        self.assertFalse(self.__pawn_black__.is_valid_move(1, 0, 2, 1, self.__empty_board__))


    # ===== Captura inválida porque la pieza en la casilla destino es del mismo color =====
    def test_invalid_capture_same_color(self):
        self.__empty_board__[5][1] = Piece('white')
        self.assertFalse(self.__pawn_white__.is_valid_move(6, 0, 5, 1, self.__empty_board__))

        self.__empty_board__[2][1] = Piece('black')
        self.assertFalse(self.__pawn_black__.is_valid_move(1, 0, 2, 1, self.__empty_board__))

if __name__ == '__main__':
    unittest.main()
