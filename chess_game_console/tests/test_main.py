import unittest
from main import Chess

class TestChessMain(unittest.TestCase):

    def setUp(self):
        # Inicializa una nueva partida de ajedrez antes de cada prueba.
        self.game = Chess()

    def test_initial_turn(self):
        # Verifica que el turno inicial sea del jugador blanco.
        self.assertEqual(self.game.current_turn, 'white', "El turno inicial debe ser de las blancas.")

    def test_toggle_turn(self):
        # Verifica que el turno alterna correctamente entre los jugadores.
        self.game.toggle_turn()  # Cambia el turno una vez
        self.assertEqual(self.game.current_turn, 'black', "El turno debe alternar a las negras.")
        self.game.toggle_turn()  # Cambia el turno nuevamente
        self.assertEqual(self.game.current_turn, 'white', "El turno debe alternar nuevamente a las blancas.")

    def test_handle_valid_command(self):
        # Verifica que un comando de movimiento válido se maneje correctamente.
        command = 'mover e2 e4'  # Comando válido para mover el peón blanco
        self.game.handle_command(command)  # Procesa el comando
        self.assertIsNone(self.game.board.grid[6][4], "La posición 'e2' debe estar vacía después del movimiento.")
        self.assertIsNotNone(self.game.board.grid[4][4], "Debe haber una pieza en 'e4' después del movimiento.")

    def test_handle_invalid_command(self):
        # Verifica que un comando inválido sea detectado.
        command = 'mover e1 e5'  # Comando inválido (no se puede mover el rey a e5)
        self.game.handle_command(command)
        self.assertIsNotNone(self.game.board.grid[7][4], "El rey debe permanecer en la posición 'e1' después del comando inválido.")
    
    def test_update_score(self):
        # Verifica que el puntaje se actualice correctamente tras una captura.
        # Simula la captura de un peón blanco por un peón negro
        self.game.update_score(self.game.board.grid[6][4])  # Peón blanco capturado
        self.assertEqual(self.game.score['white'], 1, "El puntaje debe aumentar para las blancas tras capturar una pieza.")
    
if __name__ == "_main_":
    unittest.main()