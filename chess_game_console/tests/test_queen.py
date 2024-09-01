import unittest
from pieces.queen import Queen
from pieces.pawn import Pawn

class TestQueen(unittest.TestCase):
    
    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.queen = Queen('white')
        self.board[3][3] = self.queen  # Colocamos la Reina en la posición d4 (3,3)

    def test_horizontal_move(self):
        # Movimiento horizontal válido
        self.assertTrue(self.queen.is_valid_move(3, 3, 3, 7, self.board))  # d4 -> h4
        
        # Movimiento horizontal bloqueado
        self.board[3][5] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 3, 7, self.board))  # d4 -> h4 (bloqueado por peón en f4)

    def test_vertical_move(self):
        # Movimiento vertical válido
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 3, self.board))  # d4 -> d7

        # Movimiento vertical bloqueado
        self.board[5][3] = Pawn('black')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 3, self.board))  # d4 -> d7 (bloqueado por peón en d6)

    def test_diagonal_move(self):
        # Movimiento diagonal válido
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7

        # Movimiento diagonal bloqueado
        self.board[5][5] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (bloqueado por peón en f6)

    def test_invalid_move(self):
        # Movimiento no válido (en L como un caballo)
        self.assertFalse(self.queen.is_valid_move(3, 3, 5, 4, self.board))  # d4 -> e6 (no válido)

    def test_capture_move(self):
        # Movimiento válido con captura
        self.board[6][6] = Pawn('black')
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (captura)

        # Movimiento no válido por pieza del mismo color en destino
        self.board[6][6] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (bloqueado por peón en g7)

if __name__ == "__main__":
    unittest.main()
