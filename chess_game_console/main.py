import sys                              # Manejo de argumentos del sistema.
import unittest                         # Para ejecutar pruebas unitarias.
import redis                            # Para conectarse con la base de datos Redis.
import pickle                           # Para serializar/deserializar objetos complejos.
from board.board import Board            # Clase Board que representa el tablero.
from pieces.king import King             # Clase para la pieza King.
from pieces.pawn import Pawn             # Clase para la pieza Pawn.
from pieces.rook import Rook             # Clase para la pieza Rook.
from pieces.knight import Knight         # Clase para la pieza Knight.
from pieces.bishop import Bishop         # Clase para la pieza Bishop.
from pieces.queen import Queen           # Clase para la pieza Queen.




# ===== Clase principal para el manejo del juego de ajedrez =====
class Chess:


    def __init__(self, game_id=None):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)  # Conexión a Redis.
        self.game_id = game_id or "default_game"  # Identificador único para la partida.


        if game_id:  # Si se proporciona un game_id, intenta cargar la partida guardada.
            if self.load_game():  # Si la carga es exitosa, no inicializa el juego.
                return


        self.__board__ = Board()                # Crea el tablero de ajedrez.
        self.__current_turn__ = 'white'         # Turno inicial para el jugador con piezas blancas.
        self.__score__ = {'white': 0, 'black': 0}  # Puntuación inicial de ambos jugadores.


    # ===== Inicia el ciclo principal del juego =====
    def start(self):
        while True:                               # Bucle principal del juego.
            self.__board__.display()              # Muestra el tablero.
            print(f"Turno actual: {self.__current_turn__}")  # Muestra el turno actual.
            print(f"Puntaje - Blanco: {self.__score__['white']}, Negro: {self.__score__['black']}")  # Muestra el puntaje.


            command = input("Introduce tu movimiento o comando ('mover <origen> <destino>', 'capturas', 'guardar', 'salir'): ")


            if command == 'salir':               # Si el jugador decide salir, termina el juego.
                print("Gracias por jugar.")
                exit()
           
            elif command == 'guardar':           # Si el jugador elige 'guardar', guarda el estado del juego.
                self.save_game()
                print("Juego guardado correctamente.")
                continue
           
            elif command == 'capturas':          # Muestra las piezas capturadas.
                self.show_captured_pieces()
                continue
           
            self.handle_command(command)         # Maneja los movimientos del jugador.


    # ===== Guarda el estado actual del juego en Redis =====
    def save_game(self):
        game_state = {
            'board': pickle.dumps(self.__board__),      # Serializa el objeto del tablero.
            'current_turn': self.__current_turn__,      # Almacena el turno actual.
            'score': self.__score__                    # Almacena el puntaje actual.
        }
        # Guardamos cada campo del estado del juego en Redis usando hset()
        for key, value in game_state.items():
            self.redis_client.hset(self.game_id, key, value)  # Guarda los datos en Redis
        print("Partida guardada correctamente.")


    # ===== Carga el estado del juego desde Redis si existe =====
    def load_game(self):
        if self.redis_client.exists(self.game_id):  # Verifica si existe un estado guardado
            game_state = self.redis_client.hgetall(self.game_id)
            self.__board__ = pickle.loads(game_state[b'board'])  # Carga el tablero deserializado
            self.__current_turn__ = game_state[b'current_turn'].decode('utf-8')  # Carga el turno actual
            self.__score__ = pickle.loads(game_state[b'score'])  # Carga el puntaje
            print("Partida cargada correctamente.")
        else:
            print("No se encontró una partida guardada.")


    # ===== Procesa el comando del jugador =====
    def handle_command(self, command):
        parts = command.split()                             # Divide el comando en partes.
        if len(parts) == 3 and parts[0] == 'mover':         # Si el comando es un movimiento válido.
            start, end = parts[1], parts[2]                 # Extrae las posiciones de inicio y fin.
            captured_piece = self.__board__.move_piece(start, end, self.__current_turn__)  # Realiza el movimiento.


            if captured_piece:                              # Si una pieza es capturada, actualiza el puntaje.
                self.update_score(captured_piece)
                if isinstance(captured_piece, King):        # Si el rey es capturado, el juego termina.
                    print(f"El {captured_piece.color} Rey ha sido capturado. ¡El juego ha terminado!")
                    exit()
           
            self.toggle_turn()                              # Cambia el turno al siguiente jugador.
        else:
            print("Comando no válido. Ejemplo de uso: 'mover e2 e4'")


    # ===== Cambia el turno entre jugadores =====
    def toggle_turn(self):
        self.__current_turn__ = 'black' if self.__current_turn__ == 'white' else 'white'


    # ===== Actualiza el puntaje del jugador =====
    def update_score(self, piece_captured):
        piece_values = {           # Define el valor de cada pieza.
            'Pawn': 1,
            'Knight': 3,
            'Bishop': 3,
            'Rook': 5,
            'Queen': 9
        }
        captured_piece_value = piece_values.get(piece_captured.__class__.__name__, 0)
        self.__score__[self.__current_turn__] += captured_piece_value
        print(f"¡Has ganado {captured_piece_value} puntos por capturar un {piece_captured.__class__.__name__}!")


    # ===== Muestra las piezas capturadas por cada jugador =====
    def show_captured_pieces(self):
        white_captures = [piece.symbol() for piece in self.__board__.get_captured_pieces('white')]
        black_captures = [piece.symbol() for piece in self.__board__.get_captured_pieces('black')]
        print(f"Piezas capturadas por blanco: {' '.join(black_captures) if black_captures else 'Ninguna'}")
        print(f"Piezas capturadas por negro: {' '.join(white_captures) if white_captures else 'Ninguna'}")




# ===== Inicia el juego o ejecuta pruebas =====
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        loader = unittest.TestLoader()
        tests = loader.discover('tests')
        testRunner = unittest.TextTestRunner()
        testRunner.run(tests)
    else:
        game_id = input("Introduce el ID de la partida o presiona enter para iniciar una nueva: ")
        game = Chess(game_id if game_id else None)  # Inicia una nueva partida o carga la existente.
        game.start()


#Albarracín Gonzalo Nahuel
