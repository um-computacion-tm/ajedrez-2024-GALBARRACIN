# tests/test_queen.py

import unittest
from pieces.queen import Queen
from pieces.pawn import Pawn

class TestQueen(unittest.TestCase):
   
    def setUp(self):
        """
        Configura el tablero y coloca una reina blanca en d4 (posición 3,3).
        """
        self.board = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío de 8x8
        self.queen = Queen('white')
        self.board[3][3] = self.queen  # Colocamos la Reina en la posición d4 (3,3)

    # ===== Movimiento horizontal válido =====
    def test_horizontal_move(self):
        """
        Verifica que la Reina pueda moverse horizontalmente sin obstáculos y que el movimiento se invalide si hay un bloqueo.
        """
        self.assertTrue(self.queen.is_valid_move(3, 3, 3, 7, self.board))  # d4 -> h4
        
        # Movimiento horizontal bloqueado
        self.board[3][5] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 3, 7, self.board))  # d4 -> h4 (bloqueado por peón en f4)

    # ===== Movimiento vertical válido =====
    def test_vertical_move(self):
        """
        Verifica que la Reina pueda moverse verticalmente sin obstáculos y que el movimiento se invalide si hay un bloqueo.
        """
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 3, self.board))  # d4 -> d7

        # Movimiento vertical bloqueado
        self.board[5][3] = Pawn('black')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 3, self.board))  # d4 -> d7 (bloqueado por peón en d6)

    # ===== Movimiento diagonal válido =====
    def test_diagonal_move(self):
        """
        Verifica que la Reina pueda moverse diagonalmente sin obstáculos y que el movimiento se invalide si hay un bloqueo.
        """
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7

        # Movimiento diagonal bloqueado
        self.board[5][5] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (bloqueado por peón en f6)

    # ===== Movimiento no válido (en L como un caballo) =====
    def test_invalid_move(self):
        """
        Verifica que la Reina no pueda moverse en formas no válidas como en L (al estilo de un caballo).
        """
        self.assertFalse(self.queen.is_valid_move(3, 3, 5, 4, self.board))  # d4 -> e6 (no válido)

    # ===== Movimiento válido con captura =====
    def test_capture_move(self):
        """
        Verifica que la Reina pueda capturar una pieza enemiga, pero no pueda capturar una pieza del mismo color.
        """
        self.board[6][6] = Pawn('black')
        self.assertTrue(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (captura)

        # Movimiento no válido por pieza del mismo color en destino
        self.board[6][6] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (bloqueado por peón en g7)

    # ===== Movimiento fuera del tablero =====
    def test_move_out_of_bounds(self):
        """
        Verifica que un movimiento fuera de los límites del tablero sea inválido.
        """
        with self.subTest("Movimiento fuera de los límites en filas"):
            self.assertFalse(self.queen.is_valid_move(3, 3, 8, 3, self.board))  # Fuera del tablero (fila)

        with self.subTest("Movimiento fuera de los límites en columnas"):
            self.assertFalse(self.queen.is_valid_move(3, 3, 3, 8, self.board))  # Fuera del tablero (columna)

    # ===== No puede saltar piezas =====
    def test_no_jumping(self):
        """
        Verifica que la Reina no pueda saltar sobre otras piezas.
        """
        # Bloqueo en el camino diagonal
        self.board[4][4] = Pawn('white')
        self.assertFalse(self.queen.is_valid_move(3, 3, 6, 6, self.board))  # d4 -> g7 (bloqueado por peón en e5)

if __name__ == "__main__":
    unittest.main()