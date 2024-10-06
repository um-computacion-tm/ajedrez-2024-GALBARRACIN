import unittest
from unittest.mock import patch, MagicMock
import pickle
import redis
from redis_manager import RedisManager

class TestRedisManager(unittest.TestCase):

    @patch('redis.Redis')
    def test_connect_to_redis_success(self, mock_redis):
        """Prueba que la conexión a Redis se establece correctamente."""
        mock_client = MagicMock()
        mock_redis.return_value = mock_client
        mock_client.ping.return_value = True

        # Al instanciar RedisManager, _connect_to_redis() se llama automáticamente
        manager = RedisManager()
        self.assertIsNotNone(manager.__redis_client__)
        mock_client.ping.assert_called_once()  # Asegura que solo se llama una vez

    @patch('redis.Redis')
    def test_connect_to_redis_failure(self, mock_redis):
        """Prueba que se maneja correctamente la falta de conexión a Redis."""
        mock_client = MagicMock()
        mock_redis.return_value = mock_client
        mock_client.ping.side_effect = redis.ConnectionError  # Uso correcto de ConnectionError

        manager = RedisManager()
        self.assertIsNone(manager._connect_to_redis())  # Debería retornar None si falla la conexión

    @patch('redis.Redis')
    def test_save_game_success(self, mock_redis):
        """Prueba que el juego se guarda correctamente en Redis."""
        mock_client = MagicMock()
        mock_redis.return_value = mock_client

        manager = RedisManager()
        manager.__redis_client__ = mock_client

        board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        current_turn = 'white'
        score = {'white': 0, 'black': 0}

        manager.save_game(board, current_turn, score)
        mock_client.hmset.assert_called_once_with(manager.__game_id__, {
            'board': pickle.dumps(board),
            'current_turn': current_turn,
            'score': pickle.dumps(score)
        })

    @patch('redis.Redis')
    def test_save_game_no_connection(self, mock_redis):
        """Prueba que no se puede guardar el juego si no hay conexión a Redis."""
        manager = RedisManager()
        manager.__redis_client__ = None

        board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        current_turn = 'white'
        score = {'white': 0}

        with patch('builtins.print') as mock_print:
            manager.save_game(board, current_turn, score)
            mock_print.assert_called_once_with("No hay conexión a Redis, no se puede guardar la partida.")

    @patch('redis.Redis')
    def test_load_game_success(self, mock_redis):
        """Prueba que se puede cargar el juego correctamente desde Redis."""
        mock_client = MagicMock()
        mock_redis.return_value = mock_client

        board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        current_turn = 'white'
        score = {'white': 0, 'black': 0}

        game_state = {
            b'board': pickle.dumps(board),
            b'current_turn': current_turn.encode('utf-8'),
            b'score': pickle.dumps(score)
        }

        mock_client.exists.return_value = True
        mock_client.hgetall.return_value = game_state

        manager = RedisManager()
        manager.__redis_client__ = mock_client

        loaded_board, loaded_turn, loaded_score = manager.load_game()
        self.assertEqual(loaded_board, board)
        self.assertEqual(loaded_turn, current_turn)
        self.assertEqual(loaded_score, score)

    @patch('redis.Redis')
    def test_load_game_no_connection(self, mock_redis):
        """Prueba que no se puede cargar el juego si no hay conexión a Redis."""
        manager = RedisManager()
        manager.__redis_client__ = None

        with patch('builtins.print') as mock_print:
            board, turn, score = manager.load_game()
            mock_print.assert_called_once_with("No hay conexión a Redis, no se puede cargar la partida.")
            self.assertIsNone(board)
            self.assertIsNone(turn)
            self.assertIsNone(score)

    @patch('redis.Redis')
    def test_load_game_no_saved_game(self, mock_redis):
        """Prueba que se maneja correctamente cuando no hay una partida guardada en Redis."""
        mock_client = MagicMock()
        mock_redis.return_value = mock_client

        mock_client.exists.return_value = False

        manager = RedisManager()
        manager.__redis_client__ = mock_client

        with patch('builtins.print') as mock_print:
            board, turn, score = manager.load_game()
            mock_print.assert_called_once_with("No se encontró una partida guardada con ID:", manager.__game_id__)
            self.assertIsNone(board)
            self.assertIsNone(turn)
            self.assertIsNone(score)

if __name__ == '__main__':
    unittest.main()
