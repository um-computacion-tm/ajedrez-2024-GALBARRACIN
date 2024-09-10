import unittest
from board.board import Board
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class TestBoard(unittest.TestCase):


    # ===== Configura un tablero nuevo antes de cada prueba. =====
    def setUp(self):
        self.board = Board()


    # ===== Verifica que las piezas se coloquen correctamente en sus posiciones iniciales. =====
    def test_initial_setup(self):
        
        # Verifica los peones negros en la fila 1
        for col in range(8):
            self.assertIsInstance(self.board.grid[1][col], Pawn)
            self.assertEqual(self.board.grid[1][col].color, 'black')

        # Verifica los peones blancos en la fila 6
        for col in range(8):
            self.assertIsInstance(self.board.grid[6][col], Pawn)
            self.assertEqual(self.board.grid[6][col].color, 'white')

        # Verifica las demás piezas negras en la fila 0
        expected_black = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(expected_black):
            self.assertIsInstance(self.board.grid[0][col], piece_class)
            self.assertEqual(self.board.grid[0][col].color, 'black')

        # Verifica las demás piezas blancas en la fila 7
        expected_white = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(expected_white):
            self.assertIsInstance(self.board.grid[7][col], piece_class)
            self.assertEqual(self.board.grid[7][col].color, 'white')


    # ===== Verifica que una pieza se mueva correctamente a una nueva posición. =====
    def test_move_piece_valid(self):
        # Mueve un peón blanco de e2 a e4
        self.board.move_piece('e2', 'e4', 'white')
        self.assertIsInstance(self.board.grid[4][4], Pawn)
        self.assertIsNone(self.board.grid[6][4])  # La posición inicial debe estar vacía.


     # ===== Verifica que no se permita mover una pieza de manera inválida. =====
    def test_move_piece_invalid(self):

        # Intenta mover una pieza de una casilla vacía
        result = self.board.move_piece('e3', 'e5', 'white')
        self.assertIsNone(result)


    # ===== Verifica que una captura ocurra correctamente y que la pieza capturada se añada a la lista correspondiente. =====
    def test_capture_piece(self):
        # Mueve un peón blanco de e2 a e4
        self.board.move_piece('e2', 'e4', 'white')

        # Mueve un peón negro de d7 a d5
        self.board.move_piece('d7', 'd5', 'black')

        # Captura el peón negro con el peón blanco
        captured = self.board.move_piece('e4', 'd5', 'white')
        self.assertIsInstance(captured, Pawn)
        self.assertIn(captured, self.board.captured_pieces_black)  # Verificamos que la pieza capturada está en la lista de capturas de blancas.


    # ===== Verifica que se puedan obtener las piezas capturadas correctamente. =====
    def test_get_captured_pieces(self):
        # Mueve un peón blanco de e2 a e4
        self.board.move_piece('e2', 'e4', 'white')

        # Mueve un peón negro de d7 a d5
        self.board.move_piece('d7', 'd5', 'black')

        # Captura el peón negro con el peón blanco
        captured = self.board.move_piece('e4', 'd5', 'white')
        self.assertIn(captured, self.board.get_captured_pieces('white'))

if __name__ == '__main__':
    unittest.main()
