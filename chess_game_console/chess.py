# chess.py
from board.board import Board
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class Chess:
    """
    Clase principal que controla la lógica del juego.
    """
    def __init__(self):
        # Inicializamos el tablero del juego
        self.board = Board()
        # El juego inicia con el jugador blanco
        self.current_turn = 'white'
        # Inicializa el puntaje para ambos jugadores
        self.score = {'white': 0, 'black': 0}

    def start(self):
        """
        Método que inicia el juego y permite la interacción con los jugadores.
        """
        while True:
            self.board.display()
            print(f"Turno actual: {self.current_turn}")
            print(f"Puntaje - Blanco: {self.score['white']}, Negro: {self.score['black']}")
            command = input("Introduce tu movimiento o comando ('mover origen destino', 'salir'): ")

            if command == 'salir':
                print("Gracias por jugar.")
                exit()

            self.handle_command(command)

    def handle_command(self, command):
        """
        Procesa el comando ingresado por el jugador.
        """
        parts = command.split()
        if len(parts) == 3 and parts[0] == 'mover':
            start, end = parts[1], parts[2]
            if self.board.move_piece(start, end, self.current_turn):
                self.toggle_turn()
        else:
            print("Comando no válido. Ejemplo de uso: 'mover e2 e4'")

    def toggle_turn(self):
        """
        Cambia el turno del jugador actual.
        """
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def update_score(self, piece_captured):
        """
        Actualiza el puntaje cuando una pieza es capturada.
        """
        piece_values = {'Pawn': 1, 'Knight': 3, 'Bishop': 3, 'Rook': 5, 'Queen': 9}
        if piece_captured:
            self.score[self.current_turn] += piece_values.get(piece_captured.__class__.__name__, 0)


# Ejecución del juego
if __name__ == "__main__":
    game = Chess()
    game.start()
