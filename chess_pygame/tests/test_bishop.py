import unittest
from board.board import black_locations, white_locations
from pieces.bishop import check_bishop 

class TestBishopMoves(unittest.TestCase):

    def setUp(self):
        # Reiniciar las posiciones antes de cada prueba
        global black_locations, white_locations
        black_locations = []
        white_locations = []

    def test_bishop_moves_no_obstacles(self):
        # Alfil en el centro del tablero, sin obstrucciones
        position = (4, 4)
        expected_moves = [(5, 3), (6, 2), (7, 1), (3, 3), (2, 2), (1, 1), (0, 0), 
                          (5, 5), (6, 6), (7, 7), (3, 5), (2, 6), (1, 7)]
        self.assertEqual(set(check_bishop(position, 'white')), set(expected_moves))

    def test_bishop_moves_blocked_by_friendly(self):
        # Alfil en el centro del tablero, con piezas aliadas bloqueando algunas direcciones
        global white_locations
        white_locations = [(5, 3), (3, 5)]
        position = (4, 4)
        expected_moves = [(3, 3), (2, 2), (1, 1), (0, 0), 
                          (5, 5), (6, 6), (7, 7), (5, 3), (3, 5)]
        self.assertEqual(set(check_bishop(position, 'white')), set(expected_moves))

    def test_bishop_moves_blocked_by_enemy(self):
        # Alfil en el centro del tablero, con piezas enemigas bloqueando algunas direcciones
        global black_locations
        black_locations = [(5, 3), (3, 5)]
        position = (4, 4)
        expected_moves = [(5, 3), (3, 3), (2, 2), (1, 1), (0, 0), 
                          (5, 5), (6, 6), (7, 7), (3, 5)]
        self.assertEqual(set(check_bishop(position, 'white')), set(expected_moves))

    def test_bishop_corner_no_obstacles(self):
        # Alfil en una esquina del tablero, sin obstrucciones
        position = (0, 0)
        expected_moves = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
        self.assertEqual(set(check_bishop(position, 'white')), set(expected_moves))

    def test_bishop_corner_blocked(self):
        # Alfil en una esquina del tablero, bloqueado por una pieza aliada en la diagonal
        global white_locations
        white_locations = [(1, 1)]
        position = (0, 0)
        expected_moves = []
        self.assertEqual(set(check_bishop(position, 'white')), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
