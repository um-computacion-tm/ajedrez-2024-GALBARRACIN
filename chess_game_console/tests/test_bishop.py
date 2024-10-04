# tests/test_bishop.py

import unittest
from pieces.bishop import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        """
        Configura el estado inicial para las pruebas.
        Crea un alfil blanco y uno negro, y un tablero vacío.
        """
        self.white_bishop = Bishop('white')
        self.black_bishop = Bishop('black')
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]  # Tablero vacío de 8x8

    def test_symbol(self):
        """
        Verifica que el símbolo devuelto para el alfil sea correcto.
        'B' para el alfil blanco y 'b' para el alfil negro.
        """
        self.assertEqual(self.white_bishop.symbol(), 'B')
        self.assertEqual(self.black_bishop.symbol(), 'b')

    def test_valid_move_diagonal_no_obstacles(self):
        """
        Verifica que el alfil pueda moverse en diagonal sin obstáculos en el camino.
        """
        # Movimiento diagonal hacia adelante
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 5, 3, self.empty_board))
        # Movimiento diagonal hacia atrás
        self.assertTrue(self.white_bishop.is_valid_move(5, 3, 2, 0, self.empty_board))

    def test_invalid_move_not_diagonal(self):
        """
        Verifica que el alfil no pueda moverse si no es un movimiento diagonal.
        """
        # Movimiento vertical (no diagonal)
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 3, 0, self.empty_board))
        # Movimiento horizontal (no diagonal)
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 2, 2, self.empty_board))

    def test_invalid_move_out_of_bounds(self):
        """
        Verifica que el alfil no pueda moverse fuera de los límites del tablero.
        """
        # Movimiento fuera de los límites del tablero
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 9, 7, self.empty_board))
        self.assertFalse(self.white_bishop.is_valid_move(9, 7, 2, 0, self.empty_board))

    def test_valid_move_diagonal_with_obstacles(self):
        """
        Verifica que el alfil no pueda moverse si hay una pieza bloqueando su camino.
        """
        # Coloca una pieza en el camino del alfil (en la posición (3,1))
        self.empty_board[3][1] = self.black_bishop
        # El movimiento debería ser inválido debido a la obstrucción
        self.assertFalse(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))

    def test_valid_move_capture(self):
        """
        Verifica que el alfil pueda capturar una pieza enemiga.
        """
        # Coloca una pieza enemiga en la posición de destino (4,2)
        self.empty_board[4][2] = self.black_bishop
        # Movimiento válido para capturar
        self.assertTrue(self.white_bishop.is_valid_move(2, 0, 4, 2, self.empty_board))

if __name__ == '__main__':
    unittest.main()
