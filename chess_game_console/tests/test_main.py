import unittest
from unittest.mock import patch, MagicMock
from main import Chess
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King


class TestChess(unittest.TestCase):


    # ===== Método que se ejecuta antes de cada prueba, creando una instancia del juego de ajedrez. =====
    def setUp(self):
        self.chess_game = Chess()
        self.chess_game.__board__ = MagicMock()  # Mock del tablero para evitar comportamiento real del juego.


    # ===== Prueba que el turno se alterna correctamente entre 'white' y 'black'. ======
    def test_toggle_turn(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'black')

        self.chess_game.toggle_turn()
        self.assertEqual(self.chess_game.__current_turn__, 'white')


    # ===== Prueba que un comando inválido no cambia el turno ni afecta el juego. =====
    def test_handle_command_invalid(self):
        invalid_command = "invalid command"
        with patch('builtins.print') as mocked_print:
            self.chess_game.handle_command(invalid_command)
            mocked_print.assert_called_with("Comando no válido. Ejemplo de uso: 'mover e2 e4'")


    # ===== Prueba que un movimiento válido llama a la función move_piece del tablero y alterna el turno. ======
    def test_handle_command_move(self):
        valid_command = "mover e2 e4"
        self.chess_game.__current_turn__ = 'white'

        self.chess_game.__board__.move_piece.return_value = None  # No hay captura de pieza.

        with patch.object(self.chess_game, 'toggle_turn') as mocked_toggle:
            self.chess_game.handle_command(valid_command)
            self.chess_game.__board__.move_piece.assert_called_once_with('e2', 'e4', 'white')
            mocked_toggle.assert_called_once()


    # ===== Prueba que al capturar una pieza se actualiza correctamente el puntaje. ======
    def test_update_score(self):
        self.chess_game.__current_turn__ = 'white'
        self.chess_game.__score__ = {'white': 0, 'black': 0}

        
        captured_piece = Queen('black') # Simula la captura de una Reina

        with patch('builtins.print') as mocked_print:
            self.chess_game.update_score(captured_piece)
            self.assertEqual(self.chess_game.__score__['white'], 9)  # La Reina tiene valor de 9 puntos.
            mocked_print.assert_called_with("¡Has ganado 9 puntos por capturar un Queen!")

    # ===== Prueba que el comando 'salir' termina el juego lanzando SystemExit.=====
    def test_start_exit(self):
        with patch('builtins.input', return_value='salir'), patch('builtins.print'):
            with self.assertRaises(SystemExit):  # Verifica que SystemExit sea lanzado
                self.chess_game.start()



if __name__ == "__main__":
    unittest.main()
