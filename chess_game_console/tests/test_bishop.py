import unittest                           # Importa el módulo unittest para escribir y ejecutar pruebas unitarias.
from pieces.bishop import Bishop           # Importa la clase Bishop desde el módulo pieces.bishop.

class TestBishop(unittest.TestCase):       # Define una clase de pruebas que hereda de unittest.TestCase.

    def setUp(self):                       # Método especial que se ejecuta antes de cada prueba.
        self.white_bishop = Bishop('white')    # Crea una instancia de Bishop de color blanco.
        self.black_bishop = Bishop('black')    # Crea una instancia de Bishop de color negro.
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]  # Inicializa un tablero vacío de 8x8.

    def test_symbol(self):                 # Prueba el método que devuelve el símbolo del alfil.
        self.assertEqual(self.white_bishop.symbol(), 'B')  # Verifica que el símbolo del alfil blanco sea 'B'.
        self.assertEqual(self.black_bishop.symbol(), 'b')  # Verifica que el símbolo del alfil negro sea 'b'.

    def test_valid_move_diagonal_no_obstacles(self):  # Prueba movimientos válidos en diagonal sin obstáculos.
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 5, 3, self.empty_board))  # Diagonal hacia adelante.
        self.assertTrue(self.white_bishop.is_valid_move(5, 3, 2, 0, self.empty_board))  # Diagonal hacia atrás.

    def test_invalid_move_not_diagonal(self):  # Prueba movimientos inválidos (no diagonales).
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 3, 0, self.empty_board))  # Movimiento vertical.
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 2, 2, self.empty_board))  # Movimiento horizontal.

    def test_invalid_move_out_of_bounds(self):  # Prueba movimientos fuera del tablero.
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 9, 7, self.empty_board))  # Fuera de los límites.

    def test_valid_move_diagonal_with_obstacles(self):  # Prueba un movimiento con un obstáculo en el camino.
        self.empty_board[3][1] = self.black_bishop  # Coloca un alfil negro en el camino.
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Movimiento bloqueado.

    def test_valid_move_capture(self):  # Prueba un movimiento válido que captura una pieza enemiga.
        self.empty_board[4][2] = self.black_bishop  # Coloca un alfil negro en la posición de destino.
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))  # Movimiento de captura.

if __name__ == '__main__':               # Punto de entrada para ejecutar el archivo directamente.
    unittest.main()                      # Ejecuta las pruebas unitarias.
