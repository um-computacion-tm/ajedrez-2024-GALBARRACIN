import unittest
from board.board import black_locations, white_locations
from pieces.king import check_king  

class TestKingMoves(unittest.TestCase):

    def setUp(self):
        # Reiniciar las posiciones antes de cada prueba
        global black_locations, white_locations
        black_locations = []
        white_locations = []

    def test_king_moves_no_obstacles(self):
        # Rey en el centro del tablero, sin obstrucciones
        position = (4, 4)
        expected_moves = [(5, 4), (5, 5), (5, 3), (3, 4), (3, 5), (3, 3), (4, 5), (4, 3)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

    def test_king_moves_blocked_by_friendly(self):
        # Rey en el centro del tablero, con piezas aliadas bloqueando algunas direcciones
        global white_locations
        white_locations = [(5, 4), (3, 3)]
        position = (4, 4)
        expected_moves = [(5, 5), (5, 3), (3, 4), (3, 5), (4, 5), (4, 3)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

    def test_king_moves_blocked_by_enemy(self):
        # Rey en el centro del tablero, con piezas enemigas bloqueando algunas direcciones
        global black_locations
        black_locations = [(5, 4), (3, 3)]
        position = (4, 4)
        expected_moves = [(5, 4), (5, 5), (5, 3), (3, 4), (3, 5), (3, 3), (4, 5), (4, 3)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

    def test_king_corner_no_obstacles(self):
        # Rey en una esquina del tablero, sin obstrucciones
        position = (0, 0)
        expected_moves = [(1, 0), (1, 1), (0, 1)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

    def test_king_corner_blocked(self):
        # Rey en una esquina del tablero, bloqueado por piezas aliadas
        global white_locations
        white_locations = [(1, 0), (0, 1)]
        position = (0, 0)
        expected_moves = [(1, 1)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

    def test_king_on_edge(self):
        # Rey en el borde del tablero, sin obstrucciones
        position = (0, 4)
        expected_moves = [(1, 4), (1, 5), (1, 3), (0, 5), (0, 3)]
        self.assertEqual(set(check_king(position, 'white')), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
