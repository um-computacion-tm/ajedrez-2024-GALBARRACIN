import unittest
from unittest.mock import patch, MagicMock
from main import Chess


class TestChessMain(unittest.TestCase):

    def setUp(self):
        # Inicializa una nueva partida de ajedrez antes de cada prueba.
        self.game = Chess()

    def test_initial_turn(self):
        # Verifica que el turno inicial sea del jugador blanco.
        self.assertEqual(self.game.get_current_turn(), 'white', "El turno inicial debe ser de las blancas.")

    def test_toggle_turn(self):
        # Verifica que el turno alterna correctamente entre los jugadores.
        self.game.toggle_turn()  # Cambia el turno una vez
        self.assertEqual(self.game.get_current_turn(), 'black', "El turno debe alternar a las negras.")
        self.game.toggle_turn()  # Cambia el turno nuevamente
        self.assertEqual(self.game.get_current_turn(), 'white', "El turno debe alternar nuevamente a las blancas.")

    @patch('builtins.input', side_effect=['salir'])
    @patch('builtins.print')
    def test_start_game_exit(self, mock_print, mock_input):
        # Verifica que el juego se cierra correctamente cuando se introduce el comando 'salir'.
        with self.assertRaises(SystemExit):  # Esperamos que se lance SystemExit
            self.game.start()

    @patch('builtins.input', side_effect=['mover e2 e4', 'salir'])
    @patch.object(Chess, 'handle_command')
    def test_start_game_handle_move(self, mock_handle_command, mock_input):
        # Verifica que el método handle_command se llame al introducir un comando de movimiento válido.
        with self.assertRaises(SystemExit):  # Esperamos que se lance SystemExit al final
            self.game.start()
        mock_handle_command.assert_called_with('mover e2 e4')

    @patch.object(Chess, 'handle_command')
    def test_handle_valid_command(self, mock_handle_command):
        # Verifica que un comando de movimiento válido se maneje correctamente.
        command = 'mover e2 e4'  # Comando válido para mover el peón blanco
        self.game.handle_command(command)  # Procesa el comando
        mock_handle_command.assert_called_with(command)

    def test_handle_invalid_command(self):
        # Verifica que un comando inválido sea detectado.
        command = 'mover e1 e5'  # Comando inválido (no se puede mover el rey a e5)
        with patch('builtins.print') as mock_print:
            self.game.handle_command(command)
            mock_print.assert_called_with("Comando no válido. Ejemplo de uso: 'mover e2 e4'")

    @patch.object(Chess, 'update_score')
    def test_update_score(self, mock_update_score):
        # Simula la captura de un peón blanco
        piece = MagicMock()
        piece.__class__.__name__ = 'Pawn'
        self.game.update_score(piece)
        mock_update_score.assert_called_with(piece)

    def test_update_score_with_no_capture(self):
        # Verifica que el puntaje no cambie si no se captura ninguna pieza.
        current_score = self.game.get_score()['white']
        self.game.update_score(None)  # No se captura ninguna pieza
        self.assertEqual(self.game.get_score()['white'], current_score, "El puntaje no debe cambiar si no se captura ninguna pieza.")

    def test_handle_command_invalid_format(self):
        # Verifica que un comando con formato incorrecto no cause errores.
        command = 'incorrecto e2 e4'  # Comando con formato incorrecto
        with patch('builtins.print') as mocked_print:
            self.game.handle_command(command)
            mocked_print.assert_called_with("Comando no válido. Ejemplo de uso: 'mover e2 e4'")

    def test_start_score_display(self):
        # Verifica que el puntaje se muestre correctamente al inicio del juego.
        with patch('builtins.input', side_effect=['salir']):
            with patch('builtins.print') as mock_print:
                with self.assertRaises(SystemExit):
                    self.game.start()
                mock_print.assert_any_call("Puntaje - Blanco: 0, Negro: 0")


if __name__ == "__main__":
    unittest.main()