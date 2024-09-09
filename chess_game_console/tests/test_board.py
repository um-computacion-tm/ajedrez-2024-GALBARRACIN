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
        grid = self.board.get_grid()  # Usa el getter en lugar de acceder directamente a la variable privada
        self.assertIsInstance(grid[1][0], Pawn)
        self.assertIsInstance(grid[0][0], Rook)
        self.assertIsInstance(grid[0][1], Knight)
        self.assertIsInstance(grid[0][2], Bishop)
        self.assertIsInstance(grid[0][3], Queen)
        self.assertIsInstance(grid[0][4], King)

        self.assertIsInstance(grid[6][0], Pawn)
        self.assertIsInstance(grid[7][0], Rook)
        self.assertIsInstance(grid[7][1], Knight)
        self.assertIsInstance(grid[7][2], Bishop)
        self.assertIsInstance(grid[7][3], Queen)
        self.assertIsInstance(grid[7][4], King)

    def test_move_piece_valid(self):
        # Verifica que se pueda mover una pieza válida
        self.assertTrue(self.board.move_piece("e2", "e4", "white"))  # Movimiento válido del peón blanco
        grid = self.board.get_grid()  # Usa el getter
        self.assertIsInstance(grid[4][4], Pawn)  # El peón se movió a la nueva posición
        self.assertIsNone(grid[6][4])  # La posición inicial está vacía

    def test_move_piece_invalid(self):
        # Verifica que no se pueda mover una pieza de manera inválida
        self.assertFalse(self.board.move_piece("e2", "e5", "white"))  # Movimiento inválido del peón
        grid = self.board.get_grid()  # Usa el getter
        self.assertIsInstance(grid[6][4], Pawn)  # La pieza no se movió
        self.assertIsNone(grid[3][4])  # La posición destino no cambió

    def test_invalid_color_move(self):
        # Verifica que no se pueda mover una pieza del color incorrecto
        self.assertFalse(self.board.move_piece("e7", "e5", "white"))  # Movimiento de una pieza negra con el turno de blanco

    def test_capture_piece(self):
        # Verifica que se pueda capturar una pieza
        self.board.move_piece("e2", "e4", "white")
        self.board.move_piece("d7", "d5", "black")
        self.assertTrue(self.board.move_piece("e4", "d5", "white"))  # El peón blanco captura el peón negro
        grid = self.board.get_grid()  # Usa el getter
        self.assertIsInstance(grid[3][3], Pawn)  # El peón blanco está en la nueva posición
        self.assertIsNone(grid[4][4])  # La posición original del peón blanco está vacía

    def test_invalid_start_position(self):
        # Verifica que no se pueda mover una pieza desde una posición vacía
        self.assertFalse(self.board.move_piece("e3", "e4", "white"))  # No hay ninguna pieza en e3

    def test_get_captured_pieces(self):
        # Verifica que se devuelvan correctamente las piezas capturadas
        self.board.move_piece("e2", "e4", "white")
        self.board.move_piece("d7", "d5", "black")
        self.board.move_piece("e4", "d5", "white")  # El peón blanco captura el peón negro

        captured_black_pieces = self.board.get_captured_pieces("white")
        self.assertEqual(len(captured_black_pieces), 1)
        self.assertIsInstance(captured_black_pieces[0], Pawn)

if __name__ == '__main__':
    unittest.main()
