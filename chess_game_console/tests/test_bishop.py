# tests/test_bishop.py

import unittest
from pieces.bishop import Bishop

class TestBishop(unittest.TestCase):

    def setUp(self):
        """
        Configura el estado inicial para las pruebas.
        Crea un alfil blanco y uno negro, y un tablero vacío.
        """
        self.__white_bishop__ = Bishop('__white__')
        self.__black_bishop__ = Bishop('__black__')
        self.__empty_board__ = [[None for __ in range(8)] for __ in range(8)]  # Tablero vacío de 8x8

    def test_symbol(self):
        """
        Verifica que el símbolo devuelto para el alfil sea correcto.
        'B' para el alfil blanco y 'b' para el alfil negro.
        """
        self.assertEqual(self.__white_bishop__.symbol(), 'B')
        self.assertEqual(self.__black_bishop__.symbol(), 'b')

    def test_valid_move_diagonal_no_obstacles(self):
        """
        Verifica que el alfil pueda moverse en diagonal sin obstáculos en el camino.
        """
        self.assertTrue(self.__white_bishop__.is_valid_move(2, 0, 5, 3, self.__empty_board__))
        self.assertTrue(self.__white_bishop__.is_valid_move(5, 3, 2, 0, self.__empty_board__))

    def test_invalid_move_not_diagonal(self):
        """
        Verifica que el alfil no pueda moverse si no es un movimiento diagonal.
        """
        self.assertFalse(self.__white_bishop__.is_valid_move(2, 0, 3, 0, self.__empty_board__))
        self.assertFalse(self.__white_bishop__.is_valid_move(2, 0, 2, 2, self.__empty_board__))

    def test_invalid_move_out_of_bounds(self):
        """
        Verifica que el alfil no pueda moverse fuera de los límites del tablero.
        """
        self.assertFalse(self.__white_bishop__.is_valid_move(2, 0, 9, 7, self.__empty_board__))
        self.assertFalse(self.__white_bishop__.is_valid_move(9, 7, 2, 0, self.__empty_board__))

    def test_valid_move_diagonal_with_obstacles(self):
        """
        Verifica que el alfil no pueda moverse si hay una pieza bloqueando su camino.
        """
        self.__empty_board__[3][1] = self.__black_bishop__
        self.assertFalse(self.__white_bishop__.is_valid_move(2, 0, 4, 2, self.__empty_board__))

    def test_valid_move_capture(self):
        """
        Verifica que el alfil pueda capturar una pieza enemiga.
        """
        self.__empty_board__[4][2] = self.__black_bishop__
        self.assertTrue(self.__white_bishop__.is_valid_move(2, 0, 4, 2, self.__empty_board__))

if __name__ == '__main__':
    unittest.main()
