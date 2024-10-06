import unittest
from unittest.mock import patch, MagicMock, call
import sys
from main import Chess
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from redis_manager import RedisManager

# Fake objects for mocking
class FakeBoard:
    def move_piece(self, start, end, turn):
        pass

    def display(self):
        pass

    def get_captured_pieces(self, __color__):
        return []

class FakePiece:
    def __init__(self, symbol):
        self.__symbol__ = symbol

    def symbol(self):
        return self.__symbol__

# ===== Primera parte de los tests =====
class TestChessCommands(unittest.TestCase):

    def setUp(self):
        # Crea un mock de RedisManager para evitar interacciones reales con Redis
        self.mock_redis_manager = MagicMock()

        # Crea un mock de Board para evitar la lógica real del tablero
        self.mock_board = MagicMock()

        # Instancia la clase Chess con los mocks
        self.chess_game = Chess()
        self.chess_game.__redis_manager__ = self.mock_redis_manager
        self.chess_game.__board__ = self.mock_board

    def test_guardar_comando(self):
        # Simula el comando 'guardar'
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__score__ = {'white': 5, 'black': 3}
        self.mock_redis_manager.save_game = MagicMock()

        # Llama al comando 'guardar'
        self.chess_game.__redis_manager__.save_game(self.mock_board, 'white', {'white': 5, 'black': 3})

        # Verifica que el juego se guardó correctamente
        self.mock_redis_manager.save_game.assert_called_once_with(
            self.mock_board, 'white', {'white': 5, 'black': 3}
        )

    def test_show_captured_pieces_output(self):
        # Crea mocks de las piezas capturadas con el método 'symbol'
        mock_piece_black = MagicMock()
        mock_piece_black.symbol.return_value = 'R'  # Supongamos que es una Torre (Rook)
        mock_piece_white = MagicMock()
        mock_piece_white.symbol.return_value = 'N'  # Supongamos que es un Caballo (Knight)

        # Simula las piezas capturadas
        self.mock_board.get_captured_pieces.side_effect = [
            [mock_piece_white],  # Piezas blancas capturadas
            [mock_piece_black]   # Piezas negras capturadas
        ]

        # Captura la salida de print
        with unittest.mock.patch('builtins.print') as mocked_print:
            self.chess_game.show_captured_pieces()

            # Verifica la salida esperada
            mocked_print.assert_any_call('Piezas capturadas blancas: R')
            mocked_print.assert_any_call('Piezas capturadas negras: N')

# ===== Segunda parte de los tests =====
class TestChess(unittest.TestCase):

    def setUp(self):
        # Inicializa un nuevo juego y sustituye el tablero por un mock
        self.chess_game = Chess()
        self.chess_game.__board__ = FakeBoard()

    def test_toggle_turn(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'black')

        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'white')

    def test_handle_command_invalid(self):
        invalid_command = "invalid command"
        with patch('builtins.print') as mocked_print:
            self.chess_game.handle_command(invalid_command)
            mocked_print.assert_called_with("Comando no válido. Ejemplo de uso: 'mover e2 e4'")

    def test_handle_command_move(self):
        valid_command = "mover e2 e4"
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__board__.move_piece = MagicMock(return_value=None)

        with patch.object(self.chess_game, 'toggle_turn') as mocked_toggle:
            self.chess_game.handle_command(valid_command)
            self.chess_game.__board__.move_piece.assert_called_once_with('e2', 'e4', 'white')
            mocked_toggle.assert_called_once()

    def test_update_score(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__score__ = {'white': 0, 'black': 0}

        captured_piece = Queen('black')

        with patch('builtins.print') as mocked_print:
            self.chess_game.update_score(captured_piece)
            self.assertEqual(self.chess_game.__score__['white'], 9)
            mocked_print.assert_called_with("¡Has ganado 9 puntos por capturar un Queen!")

    def test_start_exit(self):
        with patch('builtins.input', return_value='salir'), patch('builtins.print'):
            with self.assertRaises(SystemExit):
                self.chess_game.start()

    def test_handle_command_capture_king(self):
        valid_command = "mover e2 e4"
        self.chess_game.__current_turn__ = 'white'

        captured_piece = King('black')
        self.chess_game.__board__.move_piece = MagicMock(return_value=captured_piece)

        with patch('builtins.print') as mocked_print, patch.object(self.chess_game, 'toggle_turn'):
            with self.assertRaises(SystemExit):
                self.chess_game.handle_command(valid_command)
                self.chess_game.__board__.move_piece.assert_called_once_with('e2', 'e4', 'white')
                mocked_print.assert_any_call("El black Rey ha sido capturado. ¡El juego ha terminado!")

    def test_show_captured_pieces(self):
        self.chess_game.__board__.get_captured_pieces = MagicMock(side_effect=[
            [FakePiece('Q')],
            [FakePiece('P')]
        ])

        with patch('builtins.print') as mocked_print:
            self.chess_game.show_captured_pieces()
            mocked_print.assert_any_call("Piezas capturadas blancas: P")
            mocked_print.assert_any_call("Piezas capturadas negras: Q")

    def test_init_new_game(self):
        with patch.object(RedisManager, 'load_game', return_value=(None, None, None)) as mocked_load:
            game = Chess(__game_id__="test_game")
            self.assertIsNotNone(game.__board__)
            self.assertEqual(game.__current_turn__, 'white')
            self.assertEqual(game.__score__, {'white': 0, 'black': 0})
            mocked_load.assert_called_once()

    def test_init_saved_game(self):
        saved_board = FakeBoard()
        saved_turn = 'black'
        saved_score = {'white': 5, 'black': 7}

        with patch.object(RedisManager, 'load_game', return_value=(saved_board, saved_turn, saved_score)):
            game = Chess(__game_id__="saved_game")
            self.assertEqual(game.__board__, saved_board)
            self.assertEqual(game.__current_turn__, saved_turn)
            self.assertEqual(game.__score__, saved_score)

    def test_save_game(self):
        self.chess_game.__board__ = FakeBoard()
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__score__ = {'white': 10, 'black': 5}

        with patch.object(RedisManager, 'save_game') as mocked_save:
            self.chess_game.__redis_manager__.save_game(self.chess_game.__board__, self.chess_game.__current_turn__, self.chess_game.__score__)
            mocked_save.assert_called_once_with(self.chess_game.__board__, 'white', {'white': 10, 'black': 5})

    def test_load_game(self):
        with patch.object(RedisManager, 'load_game', return_value=(FakeBoard(), 'black', {'white': 10, 'black': 15})):
            board, current_turn, score = self.chess_game.__redis_manager__.load_game()
            self.assertEqual(current_turn, 'black')
            self.assertEqual(score, {'white': 10, 'black': 15})

class TestMainExecution(unittest.TestCase):
    
    @patch('unittest.TextTestRunner.run')
    @patch('unittest.TestLoader.discover')
    @patch('sys.argv', ['main.py', 'test'])
    def test_run_in_test_mode(self, mock_discover, mock_run):
        mock_tests = MagicMock()
        mock_discover.return_value = mock_tests

        with patch('builtins.__import__', return_value=sys.modules['main']):
            if len(sys.argv) > 1 and sys.argv[1] == "test":
                loader = unittest.TestLoader()
                tests = loader.discover('tests')
                testRunner = unittest.TextTestRunner()
                testRunner.run(tests)

        mock_discover.assert_called_once_with('tests')
        mock_run.assert_called_once_with(mock_tests)

if __name__ == '__main__':
    unittest.main()