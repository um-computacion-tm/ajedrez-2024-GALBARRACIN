import unittest
from pieces.piece import Piece

class TestPiece(unittest.TestCase):


    # ===== Test para verificar que el constructor asigne el color correctamente =====
    def test_constructor(self):
        piece = Piece("white")
        self.assertEqual(piece.color, "white")
        
        piece_black = Piece("black")
        self.assertEqual(piece_black.color, "black")
    

    # ===== Test para verificar que is_valid_move lanza NotImplementedError =====
    def test_is_valid_move_not_implemented(self):
        piece = Piece("white")
        with self.assertRaises(NotImplementedError):
            piece.is_valid_move(0, 0, 1, 1, None)  # board is None in this case for simplicity
    

    # ===== Test para verificar que symbol lanza NotImplementedError =====
    def test_symbol_not_implemented(self):
        piece = Piece("white")
        with self.assertRaises(NotImplementedError):
            piece.symbol()

if __name__ == '__main__':
    unittest.main()
