
import sys
import unittest

# ===== Archivo chess.py para Iniciar el Juego =====

from board.board import Board           # Importa la clase Board, que representa el tablero de ajedrez.
from pieces.pawn import Pawn            # Importa la clase Pawn, que representa la pieza del peón.
from pieces.rook import Rook            # Importa la clase Rook, que representa la pieza de la torre.
from pieces.knight import Knight        # Importa la clase Knight, que representa la pieza del caballo.
from pieces.bishop import Bishop        # Importa la clase Bishop, que representa la pieza del alfil.
from pieces.queen import Queen          # Importa la clase Queen, que representa la pieza de la reina.
from pieces.king import King            # Importa la clase King, que representa la pieza del rey.


# ===== Clase principal que controla la lógica del juego. =====
class Chess:                            # Define la clase Chess, que maneja la lógica general del juego de ajedrez.

    def __init__(self):                 # Método constructor que inicializa el estado inicial del juego.
        self.board = Board()            # Inicializamos el tablero del juego usando la clase Board.
        self.current_turn = 'white'     # El juego inicia con el jugador blanco, representado por la variable 'current_turn'.
        self.score = {'white': 0, 'black': 0}  # Inicializa el puntaje de los jugadores en un diccionario.


# ===== Método que inicia el juego y permite la interacción con los jugadores. =====
    def start(self):                    # Método que inicia y controla el bucle principal del juego.

        while True:                     # Bucle infinito para mantener el juego en funcionamiento hasta que se decida salir.
            self.board.display()        # Muestra el tablero actual en la pantalla.
            print(f"Turno actual: {self.current_turn}")  # Informa de quién es el turno.
            print(f"Puntaje - Blanco: {self.score['white']}, Negro: {self.score['black']}")  # Muestra el puntaje actual de ambos jugadores.
            command = input("Introduce tu movimiento o comando ('mover origen destino', 'salir'): ")  # Solicita un comando del jugador.

            if command == 'salir':      # Si el comando es 'salir', finaliza el juego.
                print("Gracias por jugar.")
                exit()

            self.handle_command(command)  # Procesa el comando ingresado por el jugador usando el método handle_command.



# ===== Procesa el comando ingresado por el jugador. =====
    def handle_command(self, command):  # Método que maneja y valida los comandos ingresados por el jugador.
        
        parts = command.split()         # Divide el comando en partes (por ejemplo, 'mover e2 e4' se convierte en ['mover', 'e2', 'e4']).
        if len(parts) == 3 and parts[0] == 'mover':  # Verifica si el comando es un movimiento válido.
            start, end = parts[1], parts[2]  # Asigna las posiciones de inicio y fin del movimiento.
            if self.board.move_piece(start, end, self.current_turn):  # Intenta mover la pieza en el tablero.
                self.toggle_turn()      # Si el movimiento es exitoso, cambia el turno al otro jugador.
        else:
            print("Comando no válido. Ejemplo de uso: 'mover e2 e4'")  # Informa al jugador si el comando no es válido.

    def toggle_turn(self):              # Método que cambia el turno del jugador actual.
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'  # Alterna entre 'white' y 'black'.

    def update_score(self, piece_captured):  # Método que actualiza el puntaje cuando se captura una pieza.
        piece_values = {'Pawn': 1, 'Knight': 3, 'Bishop': 3, 'Rook': 5, 'Queen': 9}  # Asigna un valor a cada tipo de pieza.
        if piece_captured:             # Si se captura una pieza, actualiza el puntaje del jugador actual.
            self.score[self.current_turn] += piece_values.get(piece_captured.__class__.__name__, 0)



# ===== Ejecución del juego o ejecución de tests =====
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Descubre y ejecuta todos los tests en el directorio tests/
        loader = unittest.TestLoader()
        tests = loader.discover('tests')
        testRunner = unittest.TextTestRunner()
        testRunner.run(tests)
    else:
        game = Chess()
        game.start()
