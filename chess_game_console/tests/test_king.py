import unittest
from pieces.king import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.__white_king__ = King('white')
        self.__black_king__ = King('black')

    def test_symbol(self):
        self.assertEqual(self.__white_king__.symbol(), 'K')
        self.assertEqual(self.__black_king__.symbol(), 'k')

    # ===== Movimientos válidos para un rey (una casilla en cualquier dirección) =====
    def test_valid_move(self):
        self.assertTrue(self.__white_king__.is_valid_move(4, 4, 4, 5, None))  # Derecha
        self.assertTrue(self.__white_king__.is_valid_move(4, 4, 5, 4, None))  # Abajo
        self.assertTrue(self.__white_king__.is_valid_move(4, 4, 3, 3, None))  # Diagonal arriba-izquierda
        self.assertTrue(self.__black_king__.is_valid_move(1, 1, 0, 0, None))  # Diagonal arriba-izquierda
        self.assertTrue(self.__black_king__.is_valid_move(6, 5, 5, 5, None))  # Arriba

    # ===== Movimientos inválidos para un rey (más de una casilla) =====
    def test_invalid_move(self):
        self.assertFalse(self.__white_king__.is_valid_move(4, 4, 6, 4, None))  # Abajo dos casillas
        self.assertFalse(self.__white_king__.is_valid_move(4, 4, 4, 6, None))  # Derecha dos casillas
        self.assertFalse(self.__black_king__.is_valid_move(1, 1, 3, 1, None))  # Abajo dos casillas
        self.assertFalse(self.__black_king__.is_valid_move(6, 5, 4, 7, None))  # Diagonal abajo-derecha dos casillas

if __name__ == '__main__':
    unittest.main()
