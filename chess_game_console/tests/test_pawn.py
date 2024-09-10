# tests/test_pawn.py
import unittest
from pieces.pawn import Pawn
from pieces.piece import Piece

class TestPawn(unittest.TestCase):

    # ===== Configuración básica con un tablero vacío =====
    def setUp(self):
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        self.pawn_white = Pawn('white')
        self.pawn_black = Pawn('black')


    # ===== Movimiento válido hacia adelante (una casilla) =====
    def test_valid_move_forward_one(self):
        self.assertTrue(self.pawn_white.is_valid_move(6, 0, 5, 0, self.empty_board))
        self.assertTrue(self.pawn_black.is_valid_move(1, 0, 2, 0, self.empty_board))


    # ===== Movimiento válido hacia adelante (dos casillas en el primer movimiento) =====
    def test_valid_move_forward_two(self):
        self.assertTrue(self.pawn_white.is_valid_move(6, 0, 4, 0, self.empty_board))
        self.assertTrue(self.pawn_black.is_valid_move(1, 0, 3, 0, self.empty_board))


    # ===== Movimiento inválido porque está bloqueado por otra pieza =====
    def test_invalid_move_forward_blocked(self):
        self.empty_board[5][0] = Piece('white')
        self.assertFalse(self.pawn_white.is_valid_move(6, 0, 5, 0, self.empty_board))

        self.empty_board[2][0] = Piece('black')
        self.assertFalse(self.pawn_black.is_valid_move(1, 0, 2, 0, self.empty_board))


    # ===== Movimiento inválido hacia adelante (dos casillas) porque está bloqueado por otra pieza =====
    def test_invalid_move_forward_two_blocked(self):
        self.empty_board[4][0] = Piece('white')
        self.assertFalse(self.pawn_white.is_valid_move(6, 0, 4, 0, self.empty_board))

        self.empty_board[3][0] = Piece('black')
        self.assertFalse(self.pawn_black.is_valid_move(1, 0, 3, 0, self.empty_board))


    # ===== Captura válida en diagonal =====
    def test_valid_capture(self):
        self.empty_board[5][1] = Piece('black')
        self.assertTrue(self.pawn_white.is_valid_move(6, 0, 5, 1, self.empty_board))

        self.empty_board[2][1] = Piece('white')
        self.assertTrue(self.pawn_black.is_valid_move(1, 0, 2, 1, self.empty_board))


    # ===== Captura inválida porque no hay pieza en la casilla destino =====
    def test_invalid_capture_empty(self):
        self.assertFalse(self.pawn_white.is_valid_move(6, 0, 5, 1, self.empty_board))
        self.assertFalse(self.pawn_black.is_valid_move(1, 0, 2, 1, self.empty_board))


    # ===== Captura inválida porque la pieza en la casilla destino es del mismo color =====
    def test_invalid_capture_same_color(self):
        self.empty_board[5][1] = Piece('white')
        self.assertFalse(self.pawn_white.is_valid_move(6, 0, 5, 1, self.empty_board))

        self.empty_board[2][1] = Piece('black')
        self.assertFalse(self.pawn_black.is_valid_move(1, 0, 2, 1, self.empty_board))

if __name__ == '__main__':
    unittest.main()
