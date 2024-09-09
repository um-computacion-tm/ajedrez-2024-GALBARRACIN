import unittest
from board.board import Board  # Corrige la ruta de importación
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
        self.assertIsInstance(self.board.grid[1][0], Pawn, "Debe haber un peón en 1,0 (bando blanco)")
        self.assertIsInstance(self.board.grid[0][0], Rook, "Debe haber una torre en 0,0 (bando blanco)")
        self.assertIsInstance(self.board.grid[0][1], Knight, "Debe haber un caballo en 0,1 (bando blanco)")
        self.assertIsInstance(self.board.grid[0][2], Bishop, "Debe haber un alfil en 0,2 (bando blanco)")
        self.assertIsInstance(self.board.grid[0][3], Queen, "Debe haber una reina en 0,3 (bando blanco)")
        self.assertIsInstance(self.board.grid[0][4], King, "Debe haber un rey en 0,4 (bando blanco)")

        self.assertIsInstance(self.board.grid[6][0], Pawn, "Debe haber un peón en 6,0 (bando negro)")
        self.assertIsInstance(self.board.grid[7][0], Rook, "Debe haber una torre en 7,0 (bando negro)")
        self.assertIsInstance(self.board.grid[7][1], Knight, "Debe haber un caballo en 7,1 (bando negro)")
        self.assertIsInstance(self.board.grid[7][2], Bishop, "Debe haber un alfil en 7,2 (bando negro)")
        self.assertIsInstance(self.board.grid[7][3], Queen, "Debe haber una reina en 7,3 (bando negro)")
        self.assertIsInstance(self.board.grid[7][4], King, "Debe haber un rey en 7,4 (bando negro)")

    def test_move_piece_valid(self):
        # Verifica que se pueda mover una pieza válida
        self.assertTrue(self.board.move_piece("e2", "e4", "white"), "El movimiento de peón debe ser válido")
        self.assertIsInstance(self.board.grid[4][4], Pawn, "Debe haber un peón en e4")
        self.assertIsNone(self.board.grid[6][4], "La casilla e2 debe estar vacía tras el movimiento")

    def test_move_piece_invalid(self):
        # Verifica que no se pueda mover una pieza de manera inválida
        self.assertFalse(self.board.move_piece("e2", "e5", "white"), "El movimiento de peón es inválido")
        self.assertIsInstance(self.board.grid[6][4], Pawn, "El peón debe seguir en e2 después del movimiento inválido")
        self.assertIsNone(self.board.grid[3][4], "La casilla e5 debe estar vacía")

    def test_invalid_color_move(self):
        # Verifica que no se pueda mover una pieza del color incorrecto
        self.assertFalse(self.board.move_piece("e7", "e5", "white"), "No se puede mover una pieza negra en el turno de las blancas")

    def test_capture_piece(self):
        # Verifica que se pueda capturar una pieza
        self.board.move_piece("e2", "e4", "white")
        self.board.move_piece("d7", "d5", "black")
        self.assertTrue(self.board.move_piece("e4", "d5", "white"), "El peón blanco debe capturar el peón negro")
        self.assertIsInstance(self.board.grid[3][3], Pawn, "Debe haber un peón blanco en d5 tras la captura")
        self.assertIsNone(self.board.grid[4][4], "La casilla e4 debe estar vacía tras la captura")

    def test_invalid_start_position(self):
        # Verifica que no se pueda mover una pieza desde una posición vacía
        self.assertFalse(self.board.move_piece("e3", "e4", "white"), "No debe ser posible mover una pieza desde una posición vacía")

if __name__ == '__main__':
    unittest.main()
