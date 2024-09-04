import unittest
from board.board import black_locations, white_locations
from pieces.knight import check_knight

class TestKnightMoves(unittest.TestCase):

    def setUp(self):
        # Reiniciar las posiciones antes de cada prueba
        global black_locations, white_locations
        black_locations = []
        white_locations = []

    def test_knight_moves_no_obstacles(self):
        # Caballo en el centro del tablero, sin obstrucciones
        position = (4, 4)
        expected_moves = [(5, 6), (5, 2), (6, 5), (6, 3), (3, 6), (3, 2), (2, 5), (2, 3)]
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

    def test_knight_moves_blocked_by_friendly(self):
        # Caballo en el centro del tablero, con piezas aliadas bloqueando algunas direcciones
        global white_locations
        white_locations = [(5, 6), (2, 3)]
        position = (4, 4)
        expected_moves = [(5, 2), (6, 5), (6, 3), (3, 6), (3, 2), (2, 5)]
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

    def test_knight_moves_blocked_by_enemy(self):
        # Caballo en el centro del tablero, con piezas enemigas bloqueando algunas direcciones
        global black_locations
        black_locations = [(5, 6), (2, 3)]
        position = (4, 4)
        expected_moves = [(5, 6), (5, 2), (6, 5), (6, 3), (3, 6), (3, 2), (2, 5), (2, 3)]
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

    def test_knight_corner_no_obstacles(self):
        # Caballo en una esquina del tablero, sin obstrucciones
        position = (0, 0)
        expected_moves = [(1, 2), (2, 1)]
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

    def test_knight_corner_blocked(self):
        # Caballo en una esquina del tablero, bloqueado por piezas aliadas
        global white_locations
        white_locations = [(1, 2), (2, 1)]
        position = (0, 0)
        expected_moves = []
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

    def test_knight_on_edge(self):
        # Caballo en el borde del tablero, sin obstrucciones
        position = (0, 4)
        expected_moves = [(1, 6), (1, 2), (2, 5), (2, 3)]
        self.assertEqual(set(check_knight(position, 'white')), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
