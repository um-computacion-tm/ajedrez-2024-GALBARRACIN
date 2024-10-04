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
            piece.is_valid_move(0, 0, 1, 1, None)  # board is None in this caso por simplicidad

    # ===== Test para verificar que symbol lanza NotImplementedError =====
    def test_symbol_not_implemented(self):
        piece = Piece("white")
        with self.assertRaises(NotImplementedError):
            piece.symbol()

    # ===== Test para verificar que _is_within_board funciona correctamente =====
    def test_is_within_board(self):
        piece = Piece("white")
        
        # Dentro de los límites del tablero
        self.assertTrue(piece._is_within_board(0, 0, 7, 7))
        
        # Fuera de los límites del tablero
        self.assertFalse(piece._is_within_board(-1, 0, 7, 7))
        self.assertFalse(piece._is_within_board(0, 8, 7, 7))
        self.assertFalse(piece._is_within_board(0, 0, 9, 7))
    
    # ===== Test para verificar que is_clear_path funciona correctamente =====
    def test_is_clear_path(self):
        piece = Piece("white")
        
        # Tablero vacío (None representa una casilla vacía)
        board = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        
        # Camino despejado
        self.assertTrue(piece.is_clear_path((0, 0), (0, 7), board, (0, 1)))  # Camino horizontal
        
        # Camino bloqueado
        board[0][3] = "pawn"  # Añadimos una pieza en la casilla (0,3)
        self.assertFalse(piece.is_clear_path((0, 0), (0, 7), board, (0, 1)))  # Camino bloqueado en el medio

if __name__ == '__main__':
    unittest.main()
