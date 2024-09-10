import sys                            # Importa el módulo sys para manejar argumentos del sistema.
import unittest                       # Importa el módulo unittest para ejecutar pruebas unitarias.

from board.board import Board          # Importa la clase Board, que representa el tablero de ajedrez.
from pieces.pawn import Pawn           # Importa la clase Pawn, que representa la pieza del peón.
from pieces.rook import Rook           # Importa la clase Rook, que representa la pieza de la torre.
from pieces.knight import Knight       # Importa la clase Knight, que representa la pieza del caballo.
from pieces.bishop import Bishop       # Importa la clase Bishop, que representa la pieza del alfil.
from pieces.queen import Queen         # Importa la clase Queen, que representa la pieza de la reina.
from pieces.king import King           # Importa la clase King, que representa la pieza del rey.


# ===== Clase principal que controla la lógica del juego de ajedrez. =====
class Chess:


    # ===== Inicializa el tablero de ajedrez, el turno inicial y la puntuación de los jugadores. =====
    def __init__(self):

        self.__board__ = Board()               # Crea una instancia de la clase Board para manejar el tablero.
        self.__current_turn__ = 'white'        # Define que el turno inicial es para las piezas blancas.
        self.__score__ = {'white': 0, 'black': 0}  # Inicializa un diccionario para llevar el puntaje de ambos jugadores.


    # ===== Inicia el juego y maneja el ciclo principal del juego, permitiendo a los jugadores ingresar comandos. =====
    def start(self):

        while True:                            # Bucle infinito que mantiene el juego activo.
            self.__board__.display()           # Muestra el tablero de ajedrez en su estado actual.
            print(f"Turno actual: {self.__current_turn__}")  # Indica de quién es el turno actual.
            print(f"Puntaje - Blanco: {self.__score__['white']}, Negro: {self.__score__['black']}")  # Muestra el puntaje de ambos jugadores.
            command = input("Introduce tu movimiento o comando ('mover origen destino', 'salir'): ")  # Solicita al jugador ingresar un comando.

            if command == 'salir':             # Si el jugador ingresa 'salir', se termina el juego.
                print("Gracias por jugar.")    # Muestra un mensaje de despedida.
                exit()                         # Cierra el programa.

            self.handle_command(command)       # Procesa el comando ingresado por el jugador.


    # ===== Procesa el comando ingresado por el jugador y realiza la acción correspondiente. =====
    def handle_command(self, command):
        
        """
        Parámetros:
        - command: string que contiene el comando del jugador (por ejemplo, 'mover e2 e4').
        """

        parts = command.split()                # Divide el comando en partes (ejemplo: 'mover e2 e4' en ['mover', 'e2', 'e4']).
        if len(parts) == 3 and parts[0] == 'mover':  # Verifica que el comando sea un movimiento válido.
            start, end = parts[1], parts[2]    # Asigna las posiciones de inicio y fin del movimiento.
            captured_piece = self.__board__.move_piece(start, end, self.__current_turn__)  # Intenta mover la pieza y obtener la pieza capturada.
            if captured_piece:                 # Si una pieza fue capturada, actualiza el puntaje.
                self.update_score(captured_piece)
            self.toggle_turn()                 # Si el movimiento es válido, cambia el turno al otro jugador.
        else:
            print("Comando no válido. Ejemplo de uso: 'mover e2 e4'")  # Muestra un mensaje de error si el comando no es válido.


    # ===== Cambia el turno actual del jugador, alternando entre 'white' y 'black'. =====
    def toggle_turn(self):
        self.__current_turn__ = 'black' if self.__current_turn__ == 'white' else 'white'  # Alterna entre los turnos blanco y negro.


    # ===== Actualiza el puntaje del jugador que captura una pieza y muestra el puntaje ganado. =====
    def update_score(self, piece_captured):

        """
        Parámetros:
        - piece_captured: la pieza que fue capturada.
        """

        piece_values = {
            'Pawn': 1,      # Peón (P)
            'Knight': 3,    # Caballo (N)
            'Bishop': 3,    # Alfil (B)
            'Rook': 5,      # Torre (R)
            'Queen': 9      # Reina (Q)
        }  
        
        
        captured_piece_value = piece_values.get(piece_captured.__class__.__name__, 0) # Obtiene el nombre de la clase de la pieza capturada (por ejemplo, 'Pawn', 'Knight') y busca su valor.
        
        self.__score__[self.__current_turn__] += captured_piece_value # Añade el valor de la pieza capturada al puntaje del jugador actual.

        print(f"¡Has ganado {captured_piece_value} puntos por capturar un {piece_captured.__class__.__name__}!") # Muestra el puntaje ganado al capturar la pieza.


# ===== Ejecución del juego o ejecución de tests =====
if __name__ == "__main__":                      # Verifica si el archivo se está ejecutando directamente.
    if len(sys.argv) > 1 and sys.argv[1] == "test":  # Si se pasa el argumento 'test', ejecuta las pruebas unitarias.
        loader = unittest.TestLoader()          # Crea un cargador de pruebas unitarias.
        tests = loader.discover('tests')        # Descubre y carga todas las pruebas en el directorio 'tests'.
        testRunner = unittest.TextTestRunner()  # Crea un ejecutor de pruebas unitarias que muestra los resultados en texto.
        testRunner.run(tests)                   # Ejecuta todas las pruebas descubiertas.
    else:
        game = Chess()                          # Si no se pasa el argumento 'test', inicia el juego de ajedrez.
        game.start()                            # Llama al método start() para iniciar el ciclo del juego.

#Albarracín Gonzalo Nahuel