# main.py

import sys  # Módulo para acceder a argumentos de la línea de comandos
import unittest  # Módulo para pruebas unitarias
from board.board import Board  # Importa la clase Board
from pieces.king import King  # Importa la clase King
from redis_manager import RedisManager  # Importa la clase RedisManager

# ===== Clase principal que gestiona el juego de ajedrez =====
class Chess:

    # ===== Inicialización de la partida =====
    def __init__(self, __game_id__=None):
        # Inicializa el gestor de Redis con el ID de la partida (o "default_game" si no se proporciona)
        self.__redis_manager__ = RedisManager(__game_id__ or "default_game")
        self.__game_id__ = __game_id__ or "default_game"

        # Cargar el estado del juego desde Redis
        board, current_turn, score = self.__redis_manager__.load_game()

        # Si los datos existen, cargarlos; si no, inicializar un nuevo juego
        if board and current_turn and score:
            self.__board__ = board  # Asigna el tablero cargado
            self.__current_turn__ = current_turn  # Asigna el turno actual
            self.__score__ = score  # Asigna el puntaje
        else:
            self.__board__ = Board()  # Crea un nuevo tablero
            self.__current_turn__ = 'white'  # El turno inicial es para las piezas blancas
            self.__score__ = {'white': 0, 'black': 0}  # Inicializa el puntaje de ambos jugadores

    # ===== Inicia el bucle del juego =====
    def start(self):
        while True:  # Bucle infinito para el juego
            self.__board__.display()  # Muestra el estado actual del tablero
            print(f"Turno actual: {self.__current_turn__}")  # Imprime el turno actual
            print(f"Puntaje - Blanco: {self.__score__['white']}, Negro: {self.__score__['black']}")  # Imprime el puntaje

            # Espera un comando del jugador
            command = input("Introduce tu movimiento o comando ('mover <origen> <destino>', 'capturas', 'guardar', 'salir'): ")

            if command == 'salir':  # Si el jugador quiere salir
                print("Gracias por jugar.")
                exit()
            elif command == 'guardar':  # Si el jugador quiere guardar la partida
                self.__redis_manager__.save_game(self.__board__, self.__current_turn__, self.__score__)
                print("Juego guardado correctamente.")
                continue
            elif command == 'capturas':  # Mostrar las piezas capturadas
                self.show_captured_pieces()
                continue
            # Procesar el comando de movimiento
            self.handle_command(command)

    # ===== Maneja los comandos del jugador =====
    def handle_command(self, command):
        parts = command.split()  # Divide el comando en partes
        if len(parts) == 3 and parts[0] == 'mover':  # Verifica si el comando es un movimiento válido
            start, end = parts[1], parts[2]  # Obtiene las posiciones de origen y destino
            captured_piece = self.__board__.move_piece(start, end, self.__current_turn__)  # Mueve la pieza

            if captured_piece:  # Si se capturó una pieza
                self.update_score(captured_piece)  # Actualiza el puntaje
                if isinstance(captured_piece, King):  # Si se captura el Rey, el juego termina
                    print(f"El {captured_piece.__color__} Rey ha sido capturado. ¡El juego ha terminado!")
                    exit()

            self.toggle_turn()  # Cambia el turno
        else:
            print("Comando no válido. Ejemplo de uso: 'mover e2 e4'")  # Comando no válido

    # ===== Cambia el turno del jugador =====
    def toggle_turn(self):
        # Cambia el turno entre blanco y negro
        self.__current_turn__ = 'black' if self.__current_turn__ == 'white' else 'white'

    # ===== Actualiza el puntaje cuando se captura una pieza =====
    def update_score(self, piece_captured):
        # Valores de puntaje asignados a cada pieza capturada
        piece_values = {
            'Pawn': 1,
            'Knight': 3,
            'Bishop': 3,
            'Rook': 5,
            'Queen': 9
        }
        captured_piece_value = piece_values.get(piece_captured.__class__.__name__, 0)  # Obtiene el valor de la pieza capturada
        self.__score__[self.__current_turn__] += captured_piece_value  # Actualiza el puntaje del jugador actual
        print(f"¡Has ganado {captured_piece_value} puntos por capturar un {piece_captured.__class__.__name__}!")

    # ===== Muestra las piezas capturadas =====
    def show_captured_pieces(self):
        white_captures = [piece.symbol() for piece in self.__board__.get_captured_pieces('white')]  # Piezas capturadas blancas
        black_captures = [piece.symbol() for piece in self.__board__.get_captured_pieces('black')]  # Piezas capturadas negras
        print(f"Piezas capturadas blancas: {' '.join(black_captures) if black_captures else 'Ninguna'}")  # Imprime capturas blancas
        print(f"Piezas capturadas negras: {' '.join(white_captures) if white_captures else 'Ninguna'}")  # Imprime capturas negras


if __name__ == "__main__":
    # Si se ejecuta en modo test, correr las pruebas unitarias
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        loader = unittest.TestLoader()  # Cargador de tests
        tests = loader.discover('tests')  # Descubre todas las pruebas en la carpeta 'tests'
        testRunner = unittest.TextTestRunner()  # Define un corredor de tests
        testRunner.run(tests)  # Ejecuta las pruebas
    else:
        # Inicia un nuevo juego o carga uno existente según el ID
        __game_id__ = input("Introduce el ID de la partida o presiona enter para iniciar una nueva: ")
        game = Chess(__game_id__ if __game_id__ else None)  # Crea una nueva instancia de Chess
        game.start()  # Comienza el juego
