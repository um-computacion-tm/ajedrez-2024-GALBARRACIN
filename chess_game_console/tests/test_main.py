import unittest
from unittest.mock import patch, MagicMock, call
from main import Chess
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
import redis
import pickle

# Clase simulada de tablero para evitar problemas de serialización
class FakeBoard:
    def move_piece(self, start, end, turn):
        pass  # Implementación vacía

    def display(self):
        pass  # Método agregado para evitar el error en test_start_exit

    def get_captured_pieces(self, color):
        return []  # Lista vacía por defecto para piezas capturadas

# Clase simulada de pieza para devolver símbolos de piezas capturadas
class FakePiece:
    def __init__(self, symbol):
        self._symbol = symbol

    def symbol(self):
        return self._symbol


class TestChess(unittest.TestCase):

    # ===== Método que se ejecuta antes de cada prueba =====
    def setUp(self):
        self.chess_game = Chess()
        self.chess_game.__board__ = FakeBoard()  # Usamos FakeBoard en lugar de MagicMock
        self.chess_game.redis_client = MagicMock()  # Mock de Redis para evitar conexiones reales.

    # ===== Prueba que el turno se alterna correctamente =====
    def test_toggle_turn(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'black')

        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'white')

    # ===== Prueba que un comando inválido no cambia el turno ni afecta el juego =====
    def test_handle_command_invalid(self):
        invalid_command = "invalid command"
        with patch('builtins.print') as mocked_print:
            self.chess_game.handle_command(invalid_command)
            mocked_print.assert_called_with("Comando no válido. Ejemplo de uso: 'mover e2 e4'")

    # ===== Prueba que un movimiento válido llama a la función move_piece del tablero =====
    def test_handle_command_move(self):
        valid_command = "mover e2 e4"
        self.chess_game.__current_turn__ = 'white'

        self.chess_game.__board__.move_piece = MagicMock(return_value=None)  # No hay captura de pieza.

        with patch.object(self.chess_game, 'toggle_turn') as mocked_toggle:
            self.chess_game.handle_command(valid_command)
            self.chess_game.__board__.move_piece.assert_called_once_with('e2', 'e4', 'white')
            mocked_toggle.assert_called_once()

    # ===== Prueba que al capturar una pieza se actualiza correctamente el puntaje =====
    def test_update_score(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__score__ = {'white': 0, 'black': 0}

        captured_piece = Queen('black')  # Simula la captura de una Reina

        with patch('builtins.print') as mocked_print:
            self.chess_game.update_score(captured_piece)
            self.assertEqual(self.chess_game.__score__['white'], 9)  # La Reina tiene valor de 9 puntos.
            mocked_print.assert_called_with("¡Has ganado 9 puntos por capturar un Queen!")

    # ===== Prueba que el comando 'salir' termina el juego lanzando SystemExit =====
    def test_start_exit(self):
        with patch('builtins.input', return_value='salir'), patch('builtins.print'):
            with self.assertRaises(SystemExit):  # Verifica que SystemExit sea lanzado
                self.chess_game.start()

    # ===== Prueba que la función save_game guarda el estado correctamente =====
    def test_save_game(self):
        self.chess_game.__board__ = FakeBoard()  # Usamos FakeBoard en lugar de MagicMock
        self.chess_game.__score__ = {'white': 1, 'black': 0}

        with patch('builtins.print') as mocked_print:
            self.chess_game.save_game()

            # Verifica que Redis hset fue llamado con los valores correctos
            self.chess_game.redis_client.hset.assert_has_calls([
                call(self.chess_game.game_id, 'board', pickle.dumps(self.chess_game.__board__)),
                call(self.chess_game.game_id, 'current_turn', 'white'),
                call(self.chess_game.game_id, 'score', pickle.dumps(self.chess_game.__score__))
            ])
            mocked_print.assert_called_with(f"Partida guardada correctamente con ID: {self.chess_game.game_id}")

    # ===== Prueba que la función load_game carga el estado correctamente =====
    def test_load_game(self):
        saved_state = {
            b'board': pickle.dumps(FakeBoard()),  # Reemplazar MagicMock con FakeBoard serializable
            b'current_turn': b'white',
            b'score': pickle.dumps({'white': 1, 'black': 0})
        }
        self.chess_game.redis_client.exists.return_value = True
        self.chess_game.redis_client.hgetall.return_value = saved_state

        with patch('builtins.print') as mocked_print:
            result = self.chess_game.load_game()

            self.assertTrue(result)
            mocked_print.assert_called_with("Partida cargada correctamente.")

    # ===== Prueba que la función show_captured_pieces muestra correctamente las piezas capturadas =====
    def test_show_captured_pieces(self):
        self.chess_game.__board__.get_captured_pieces = MagicMock(side_effect=[
            [FakePiece('Q')],  # Piezas negras capturadas
            [FakePiece('P')]   # Piezas blancas capturadas
        ])

        with patch('builtins.print') as mocked_print:
            self.chess_game.show_captured_pieces()
            mocked_print.assert_any_call("Piezas capturadas blancas: P")
            mocked_print.assert_any_call("Piezas capturadas negras: Q")

    # ===== Prueba de error al cargar una partida incompleta =====
    def test_load_game_incomplete(self):
        saved_state = {b'board': pickle.dumps(FakeBoard())}  # Estado incompleto
        self.chess_game.redis_client.exists.return_value = True
        self.chess_game.redis_client.hgetall.return_value = saved_state

        with patch('builtins.print') as mocked_print:
            result = self.chess_game.load_game()

            self.assertFalse(result)
            mocked_print.assert_called_with("Datos incompletos en la partida guardada.")

    # ===== Prueba que el juego puede empezar sin conexión a Redis =====
    def test_start_without_redis(self):
        # Simula que no se puede conectar a Redis
        with patch('redis.Redis', side_effect=redis.ConnectionError), patch('builtins.print') as mocked_print:
            game = Chess()  # Inicia el juego sin Redis
            mocked_print.assert_called_with("No se pudo conectar a Redis. Continuando sin Redis...")

    # ===== Prueba que un movimiento capturando una pieza de valor actualiza el score y termina si es un Rey =====
    def test_handle_command_capture_king(self):
        valid_command = "mover e2 e4"
        self.chess_game.__current_turn__ = 'white'

        # Simula la captura de un Rey negro
        captured_piece = King('black')
        self.chess_game.__board__.move_piece = MagicMock(return_value=captured_piece)

        with patch('builtins.print') as mocked_print, patch.object(self.chess_game, 'toggle_turn'):
            with self.assertRaises(SystemExit):  # El juego debe terminar cuando se captura el Rey
                self.chess_game.handle_command(valid_command)
                self.chess_game.__board__.move_piece.assert_called_once_with('e2', 'e4', 'white')
                mocked_print.assert_any_call("El black Rey ha sido capturado. ¡El juego ha terminado!")

    # ===== Prueba que muestra el mensaje correcto cuando hay un error de Redis al guardar =====
    def test_save_game_redis_error(self):
        with patch('builtins.print') as mocked_print:
            # Simula un error de Redis al guardar el juego
            self.chess_game.redis_client.hset.side_effect = redis.ConnectionError
            self.chess_game.save_game()

            mocked_print.assert_called_with("Error al guardar la partida: ")

    # ===== Prueba que muestra el mensaje correcto cuando hay un error de Redis al cargar =====
    def test_load_game_redis_error(self):
        with patch('builtins.print') as mocked_print:
            # Simula un error de Redis al cargar el juego
            self.chess_game.redis_client.hgetall.side_effect = redis.ConnectionError
            result = self.chess_game.load_game()

            self.assertFalse(result)
            mocked_print.assert_called_with("Error al cargar la partida: ")

if __name__ == '__main__':
    unittest.main()
