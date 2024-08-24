import unittest
from main import check_king, check_queen, check_bishop, check_rook, check_knight, check_pawn

class TestChessLogic(unittest.TestCase):
    
    def setUp(self):
        # Configuración inicial de las posiciones para las pruebas
        self.white_king_position = (4, 0)
        self.black_king_position = (4, 7)
        self.white_pawn_position = (4, 1)
        self.black_pawn_position = (4, 6)
        self.white_rook_position = (0, 0)
        self.black_rook_position = (0, 7)
        
    def test_check_king(self):
        # Prueba para movimientos válidos del rey blanco
        expected_moves_white_king = [(5, 0), (5, 1), (3, 0), (3, 1), (4, 1)]
        actual_moves_white_king = check_king(self.white_king_position, 'white')
        self.assertEqual(set(actual_moves_white_king), set(expected_moves_white_king))
        
        # Prueba para movimientos válidos del rey negro
        expected_moves_black_king = [(5, 7), (5, 6), (3, 7), (3, 6), (4, 6)]
        actual_moves_black_king = check_king(self.black_king_position, 'black')
        self.assertEqual(set(actual_moves_black_king), set(expected_moves_black_king))

    def test_check_queen(self):
        # Prueba para movimientos válidos de la reina
        expected_moves_queen = check_bishop(self.white_king_position, 'white') + check_rook(self.white_king_position, 'white')
        actual_moves_queen = check_queen(self.white_king_position, 'white')
        self.assertEqual(set(actual_moves_queen), set(expected_moves_queen))

    def test_check_bishop(self):
        # Prueba para movimientos válidos del alfil
        expected_moves_bishop = [(5, 1), (6, 2), (3, 1), (2, 2)]  # Dependiendo de la posición
        actual_moves_bishop = check_bishop(self.white_king_position, 'white')
        self.assertEqual(set(actual_moves_bishop), set(expected_moves_bishop))

    def test_check_rook(self):
        # Prueba para movimientos válidos de la torre
        expected_moves_rook = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                               (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        actual_moves_rook = check_rook(self.white_rook_position, 'white')
        self.assertEqual(set(actual_moves_rook), set(expected_moves_rook))

    def test_check_knight(self):
        # Prueba para movimientos válidos del caballo
        expected_moves_knight = [(6, 1), (6, -1), (5, 2), (5, -2), (3, 2), (3, -2), (2, 1), (2, -1)]
        actual_moves_knight = check_knight(self.white_king_position, 'white')
        self.assertEqual(set(actual_moves_knight), set(expected_moves_knight))

    def test_check_pawn(self):
        # Prueba para movimientos válidos del peón blanco
        expected_moves_white_pawn = [(4, 2), (4, 3)]  # Peón en posición inicial
        actual_moves_white_pawn = check_pawn(self.white_pawn_position, 'white')
        self.assertEqual(set(actual_moves_white_pawn), set(expected_moves_white_pawn))

        # Prueba para movimientos válidos del peón negro
        expected_moves_black_pawn = [(4, 5), (4, 4)]  # Peón en posición inicial
        actual_moves_black_pawn = check_pawn(self.black_pawn_position, 'black')
        self.assertEqual(set(actual_moves_black_pawn), set(expected_moves_black_pawn))

if _name_ == '_main_':
    unittest.main()

    #ESTE TEST SE PRUEBA EN LOCAL CON EL PROYECTO TERMINADO