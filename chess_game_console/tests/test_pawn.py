import unittest
from pieces.pawn import Pawn

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.white_pawn = Pawn('white')
        self.black_pawn = Pawn('black')
        # Simulación de un tablero vacío
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]

    def test_symbol(self):
        self.assertEqual(self.white_pawn.symbol(), 'P')
        self.assertEqual(self.black_pawn.symbol(), 'p')

    def test_valid_move_one_step_forward(self):
        # Movimiento válido: un paso hacia adelante en un tablero vacío
        self.assertTrue(self.white_pawn.is_valid_move(6, 4, 5, 4, self.empty_board))  # Blanco, un paso adelante
        self.assertTrue(self.black_pawn.is_valid_move(1, 4, 2, 4, self.empty_board))  # Negro, un paso adelante

    def test_invalid_move(self):
        # Movimientos inválidos
        self.assertFalse(self.white_pawn.is_valid_move(6, 4, 4, 4, self.empty_board))  # Blanco, dos pasos sin ser primer movimiento
        self.assertFalse(self.white_pawn.is_valid_move(6, 4, 6, 5, self.empty_board))  # Blanco, movimiento lateral
        self.assertFalse(self.black_pawn.is_valid_move(1, 4, 3, 4, self.empty_board))  # Negro, dos pasos sin ser primer movimiento
        self.assertFalse(self.black_pawn.is_valid_move(1, 4, 1, 5, self.empty_board))  # Negro, movimiento lateral

    def test_blocked_move(self):
        # Movimiento inválido: otro peón bloquea el camino
        self.empty_board[5][4] = Pawn('white')  # Peón blanco bloqueando
        self.assertFalse(self.white_pawn.is_valid_move(6, 4, 5, 4, self.empty_board))  # Blanco, bloqueado

        self.empty_board[2][4] = Pawn('black')  # Peón negro bloqueando
        self.assertFalse(self.black_pawn.is_valid_move(1, 4, 2, 4, self.empty_board))  # Negro, bloqueado

if __name__ == '__main__':
    unittest.main()

#NO PASA EL TEST 