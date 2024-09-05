import unittest
from board.board import Board
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Configura un nuevo tablero antes de cada test

    def test_initial_setup(self):
        # Verifica que las piezas estén correctamente colocadas
        self.assertIsInstance(self.board.grid[1][0], Pawn)
        self.assertIsInstance(self.board.grid[0][0], Rook)
        self.assertIsInstance(self.board.grid[0][1], Knight)
        self.assertIsInstance(self.board.grid[0][2], Bishop)
        self.assertIsInstance(self.board.grid[0][3], Queen)
        self.assertIsInstance(self.board.grid[0][4], King)

        self.assertIsInstance(self.board.grid[6][0], Pawn)
        self.assertIsInstance(self.board.grid[7][0], Rook)
        self.assertIsInstance(self.board.grid[7][1], Knight)
        self.assertIsInstance(self.board.grid[7][2], Bishop)
        self.assertIsInstance(self.board.grid[7][3], Queen)
        self.assertIsInstance(self.board.grid[7][4], King)

    def test_move_piece_valid(self):
        # Verifica que se pueda mover una pieza válida
        self.assertTrue(self.board.move_piece("e2", "e4", "white"))  # Movimiento válido del peón blanco
        self.assertIsInstance(self.board.grid[4][4], Pawn)
        self.assertIsNone(self.board.grid[6][4])

    def test_move_piece_invalid(self):
        # Verifica que no se pueda mover una pieza de manera inválida
        self.assertFalse(self.board.move_piece("e2", "e5", "white"))  # Movimiento inválido del peón
        self.assertIsInstance(self.board.grid[6][4], Pawn)  # La pieza no se movió
        self.assertIsNone(self.board.grid[3][4])

    def test_invalid_color_move(self):
        # Verifica que no se pueda mover una pieza del color incorrecto
        self.assertFalse(self.board.move_piece("e7", "e5", "white"))  # Movimiento de una pieza negra con el turno de blanco

    def test_capture_piece(self):
        # Verifica que se pueda capturar una pieza
        self.board.move_piece("e2", "e4", "white")
        self.board.move_piece("d7", "d5", "black")
        self.assertTrue(self.board.move_piece("e4", "d5", "white"))  # El peón blanco captura el peón negro
        self.assertIsInstance(self.board.grid[3][3], Pawn)  # El peón blanco está en la nueva posición
        self.assertIsNone(self.board.grid[4][4])  # La posición original del peón blanco está vacía

    def test_invalid_start_position(self):
        # Verifica que no se pueda mover una pieza desde una posición vacía
        self.assertFalse(self.board.move_piece("e3", "e4", "white"))  # No hay ninguna pieza en e3

if __name__ == '__main__':
    unittest.main()