import unittest
from pieces.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.white_knight = Knight('white')
        self.black_knight = Knight('black')

    def test_symbol(self):
        self.assertEqual(self.white_knight.symbol(), 'N')
        self.assertEqual(self.black_knight.symbol(), 'n')


    # ===== Movimientos válidos para un caballo (en forma de 'L') =====
    def test_valid_move(self):
        self.assertTrue(self.white_knight.is_valid_move(4, 4, 6, 5, None))  # 2 abajo, 1 derecha
        self.assertTrue(self.white_knight.is_valid_move(4, 4, 2, 5, None))  # 2 arriba, 1 derecha
        self.assertTrue(self.black_knight.is_valid_move(3, 3, 5, 2, None))  # 2 abajo, 1 izquierda
        self.assertTrue(self.black_knight.is_valid_move(7, 7, 6, 5, None))  # 1 abajo, 2 izquierda


    # ===== Movimientos inválidos para un caballo (no en forma de 'L') =====
    def test_invalid_move(self): 
        self.assertFalse(self.white_knight.is_valid_move(4, 4, 4, 5, None))  # 1 derecha (horizontal)
        self.assertFalse(self.white_knight.is_valid_move(4, 4, 5, 4, None))  # 1 abajo (vertical)
        self.assertFalse(self.black_knight.is_valid_move(3, 3, 4, 4, None))  # 1 diagonal
        self.assertFalse(self.black_knight.is_valid_move(7, 7, 5, 7, None))  # 2 abajo (vertical)

if __name__ == '__main__':
    unittest.main()
