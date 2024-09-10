import unittest
from pieces.king import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.white_king = King('white')
        self.black_king = King('black')

    def test_symbol(self):
        self.assertEqual(self.white_king.symbol(), 'K')
        self.assertEqual(self.black_king.symbol(), 'k')


    # ===== Movimientos válidos para un rey (una casilla en cualquier dirección) =====
    def test_valid_move(self):
        self.assertTrue(self.white_king.is_valid_move(4, 4, 4, 5, None))  # Derecha
        self.assertTrue(self.white_king.is_valid_move(4, 4, 5, 4, None))  # Abajo
        self.assertTrue(self.white_king.is_valid_move(4, 4, 3, 3, None))  # Diagonal arriba-izquierda
        self.assertTrue(self.black_king.is_valid_move(1, 1, 0, 0, None))  # Diagonal arriba-izquierda
        self.assertTrue(self.black_king.is_valid_move(6, 5, 5, 5, None))  # Arriba


    # ===== Movimientos inválidos para un rey (más de una casilla) =====
    def test_invalid_move(self):
        self.assertFalse(self.white_king.is_valid_move(4, 4, 6, 4, None))  # Abajo dos casillas
        self.assertFalse(self.white_king.is_valid_move(4, 4, 4, 6, None))  # Derecha dos casillas
        self.assertFalse(self.black_king.is_valid_move(1, 1, 3, 1, None))  # Abajo dos casillas
        self.assertFalse(self.black_king.is_valid_move(6, 5, 4, 7, None))  # Diagonal abajo-derecha dos casillas

if __name__ == '__main__':
    unittest.main()
