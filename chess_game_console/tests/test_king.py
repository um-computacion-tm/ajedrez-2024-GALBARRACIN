import unittest                           # Importa el módulo unittest para realizar pruebas unitarias.
from pieces.king import King               # Importa la clase King desde el módulo pieces.king.

class TestKing(unittest.TestCase):         # Define una clase de pruebas que hereda de unittest.TestCase.

    def setUp(self):                       # Método que se ejecuta antes de cada prueba.
        self.white_king = King('white')    # Crea una instancia del rey de color blanco.
        self.black_king = King('black')    # Crea una instancia del rey de color negro.

    def test_symbol(self):                 # Prueba el método que devuelve el símbolo del rey.
        self.assertEqual(self.white_king.symbol(), 'K')  # Verifica que el símbolo del rey blanco sea 'K'.
        self.assertEqual(self.black_king.symbol(), 'k')  # Verifica que el símbolo del rey negro sea 'k'.

    def test_valid_move(self):             # Prueba los movimientos válidos del rey (una casilla en cualquier dirección).
        self.assertTrue(self.white_king.is_valid_move(4, 4, 4, 5, None))  # Movimiento válido: derecha una casilla.
        self.assertTrue(self.white_king.is_valid_move(4, 4, 5, 4, None))  # Movimiento válido: abajo una casilla.
        self.assertTrue(self.white_king.is_valid_move(4, 4, 3, 3, None))  # Movimiento válido: diagonal arriba-izquierda.
        self.assertTrue(self.black_king.is_valid_move(1, 1, 0, 0, None))  # Movimiento válido: diagonal arriba-izquierda.
        self.assertTrue(self.black_king.is_valid_move(6, 5, 5, 5, None))  # Movimiento válido: arriba una casilla.

    def test_invalid_move(self):           # Prueba movimientos inválidos para el rey (más de una casilla).
        self.assertFalse(self.white_king.is_valid_move(4, 4, 6, 4, None))  # Movimiento inválido: dos casillas hacia abajo.
        self.assertFalse(self.white_king.is_valid_move(4, 4, 4, 6, None))  # Movimiento inválido: dos casillas a la derecha.
        self.assertFalse(self.black_king.is_valid_move(1, 1, 3, 1, None))  # Movimiento inválido: dos casillas hacia abajo.
        self.assertFalse(self.black_king.is_valid_move(6, 5, 4, 7, None))  # Movimiento inválido: diagonal abajo-derecha dos casillas.

if __name__ == '__main__':                 # Punto de entrada para ejecutar el archivo directamente.
    unittest.main()                        # Ejecuta las pruebas unitarias.
