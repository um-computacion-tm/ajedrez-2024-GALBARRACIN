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
        self.__board__ = Board()

    def test_initial_setup(self):
        for col in range(8):
            self.assertIsInstance(self.__board__.__grid__[1][col], Pawn)
            self.assertEqual(self.__board__.__grid__[1][col].__color__, 'black')

        for col in range(8):
            self.assertIsInstance(self.__board__.__grid__[6][col], Pawn)
            self.assertEqual(self.__board__.__grid__[6][col].__color__, 'white')

        expected_black = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(expected_black):
            self.assertIsInstance(self.__board__.__grid__[0][col], piece_class)
            self.assertEqual(self.__board__.__grid__[0][col].__color__, 'black')

        expected_white = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece_class in enumerate(expected_white):
            self.assertIsInstance(self.__board__.__grid__[7][col], piece_class)
            self.assertEqual(self.__board__.__grid__[7][col].__color__, 'white')

    def test_move_piece_valid(self):
        self.__board__.move_piece('e2', 'e4', 'white')
        self.assertIsInstance(self.__board__.__grid__[4][4], Pawn)
        self.assertIsNone(self.__board__.__grid__[6][4])

    def test_move_piece_invalid(self):
        result = self.__board__.move_piece('e3', 'e5', 'white')
        self.assertIsNone(result)

    def test_capture_piece(self):
        self.__board__.move_piece('e2', 'e4', 'white')
        self.__board__.move_piece('d7', 'd5', 'black')
        captured = self.__board__.move_piece('e4', 'd5', 'white')
        self.assertIsInstance(captured, Pawn)
        self.assertIn(captured, self.__board__.__captured_pieces_black__)

    def test_get_captured_pieces(self):
        self.__board__.move_piece('e2', 'e4', 'white')
        self.__board__.move_piece('d7', 'd5', 'black')
        captured = self.__board__.move_piece('e4', 'd5', 'white')
        self.assertIn(captured, self.__board__.get_captured_pieces('white'))

if __name__ == '__main__':
    unittest.main()
