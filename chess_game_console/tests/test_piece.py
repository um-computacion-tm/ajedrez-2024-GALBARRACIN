import unittest
from pieces.piece import Piece

class TestPiece(unittest.TestCase):

    # ===== Test para verificar que el constructor asigne el color correctamente =====
    def test_constructor(self):
        __piece__ = Piece("white")
        self.assertEqual(__piece__.__color__, "white")
        
        piece_black = Piece("black")
        self.assertEqual(piece_black.__color__, "black")
    
    # ===== Test para verificar que is_valid_move lanza NotImplementedError =====
    def test_is_valid_move_not_implemented(self):
        __piece__ = Piece("white")
        with self.assertRaises(NotImplementedError):
            __piece__.is_valid_move(0, 0, 1, 1, None)  # board is None in this caso por simplicidad

    # ===== Test para verificar que symbol lanza NotImplementedError =====
    def test_symbol_not_implemented(self):
        __piece__ = Piece("white")
        with self.assertRaises(NotImplementedError):
            __piece__.symbol()

    # ===== Test para verificar que _is_within_board funciona correctamente =====
    def test_is_within_board(self):
        __piece__ = Piece("white")
        
        # Dentro de los límites del tablero
        self.assertTrue(__piece__._is_within_board(0, 0, 7, 7))
        
        # Fuera de los límites del tablero
        self.assertFalse(__piece__._is_within_board(-1, 0, 7, 7))
        self.assertFalse(__piece__._is_within_board(0, 8, 7, 7))
        self.assertFalse(__piece__._is_within_board(0, 0, 9, 7))
    
    # ===== Test para verificar que is_clear_path funciona correctamente =====
    def test_is_clear_path(self):
        __piece__ = Piece("white")
        
        # Tablero vacío (None representa una casilla vacía)
        __board__ = [
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
        self.assertTrue(__piece__.is_clear_path((0, 0), (0, 7), __board__, (0, 1)))  # Camino horizontal
        
        # Camino bloqueado
        __board__[0][3] = "pawn"  # Añadimos una pieza en la casilla (0,3)
        self.assertFalse(__piece__.is_clear_path((0, 0), (0, 7), __board__, (0, 1)))  # Camino bloqueado en el medio

if __name__ == '__main__':
    unittest.main()
