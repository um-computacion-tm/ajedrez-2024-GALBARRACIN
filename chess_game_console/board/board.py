# board/board.py

from pieces.pawn import Pawn      # Importa la clase Pawn, que representa la pieza del peón.
from pieces.rook import Rook      # Importa la clase Rook, que representa la pieza de la torre.
from pieces.knight import Knight  # Importa la clase Knight, que representa la pieza del caballo.
from pieces.bishop import Bishop  # Importa la clase Bishop, que representa la pieza del alfil.
from pieces.queen import Queen    # Importa la clase Queen, que representa la pieza de la reina.
from pieces.king import King      # Importa la clase King, que representa la pieza del rey.


# ===== Clase que representa el tablero de ajedrez. =====
class Board:


    # ===== Inicializa el tablero como una matriz 8x8 con las piezas en sus posiciones iniciales. =====
    def __init__(self):
        """
        También inicializa las listas para las piezas capturadas de cada jugador.
        """
        self.__grid__ = [[None for _ in range(8)] for _ in range(8)]  # Crea un tablero 8x8 con None en todas las posiciones.
        self.__captured_pieces_white__ = []  # Lista para almacenar las piezas capturadas por el jugador blanco.
        self.__captured_pieces_black__ = []  # Lista para almacenar las piezas capturadas por el jugador negro.
        self.setup_board()  # Llama al método para configurar el tablero con las piezas iniciales.


    # ===== Configura las piezas en el tablero en sus posiciones iniciales. =====
    def setup_board(self):
        # Coloca los peones blancos y negros en sus filas iniciales.
        for i in range(8):  # Itera sobre cada columna del tablero.
            self.__grid__[1][i] = Pawn('black')  # Coloca peones negros en la fila 2.
            self.__grid__[6][i] = Pawn('white')  # Coloca peones blancos en la fila 7.

        # Lista con las piezas en el orden en que se colocan en la primera y última fila.
        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        # Coloca las demás piezas para ambos jugadores.
        for i, piece in enumerate(placement):  # Itera sobre cada columna del tablero y su correspondiente pieza.
            self.__grid__[0][i] = piece('black')  # Coloca las piezas negras en la fila 1.
            self.__grid__[7][i] = piece('white')  # Coloca las piezas blancas en la fila 8.


    # ===== Muestra el tablero en la consola con las coordenadas y las piezas dentro de cuadrados. =====
    def display(self):
        def row_separator():
            return "  +" + "---+" * 8  # Genera la línea separadora entre filas.

        print("    a   b   c   d   e   f   g   h")  # Imprime las letras de las columnas en la parte superior del tablero.
        print(row_separator())  # Imprime la primera línea separadora.

        for i, row in enumerate(self.__grid__):  # Itera sobre cada fila del tablero.
            # Imprime el número de la fila y las piezas dentro de "cuadrados".
            row_pieces = f"{8 - i} | " + ' | '.join([piece.symbol() if piece else ' ' for piece in row]) + f" | {8 - i}"
            print(row_pieces)  # Imprime la fila con las piezas dentro de cuadrados.
            print(row_separator())  # Imprime la línea separadora después de cada fila.

        print("    a   b   c   d   e   f   g   h")  # Imprime las letras de las columnas en la parte inferior del tablero.


    # ===== Mueve una pieza de una posición a otra en el tablero. =====
    def move_piece(self, start, end, player_color):
        """
        Parámetros:
        - start: posición inicial en notación de ajedrez.
        - end: posición final en notación de ajedrez.
        - player_color: color del jugador que está realizando el movimiento.
        Retorna:
        - La pieza capturada, si hay alguna.
        """
        start_row, start_col = self.parse_position(start)  # Convierte la posición inicial en coordenadas (fila, columna).
        end_row, end_col = self.parse_position(end)  # Convierte la posición final en coordenadas (fila, columna).

        piece = self.__grid__[start_row][start_col]  # Obtiene la pieza en la posición inicial.
        target = self.__grid__[end_row][end_col]  # Obtiene la pieza en la posición final (si existe).

        # Verifica si hay una pieza en la posición inicial y si pertenece al jugador actual.
        if piece and piece.__color__ == player_color:
            # Verifica si el movimiento es válido para la pieza.
            if piece.is_valid_move(start_row, start_col, end_row, end_col, self.__grid__):
                captured_piece = target  # Almacena la pieza capturada.
                if captured_piece:  # Si hay una pieza en la posición final, la captura.
                    self.capture_piece(captured_piece, player_color)  # Llama al método para manejar la captura de la pieza.
                self.__grid__[end_row][end_col] = piece  # Mueve la pieza a la nueva posición.
                self.__grid__[start_row][start_col] = None  # Vacía la posición inicial.
                return captured_piece  # Retorna la pieza capturada, si hay alguna.
            else:
                print("Movimiento no válido para esa pieza.")  # Informa al jugador que el movimiento no es válido.
        else:
            print("No hay una pieza de tu color en la posición inicial.")  # Informa si la pieza no es del color correcto o no existe.
        return None  # Retorna None si no se capturó ninguna pieza.


    # ===== Maneja la captura de una pieza en el tablero, añadiéndola a la lista de piezas capturadas por el oponente. =====
    def capture_piece(self, piece, player_color):
        """
        Muestra un mensaje en la consola con la pieza capturada.
        Parámetros:
        - piece: la pieza que será capturada.
        - player_color: el color del jugador que realiza la captura.
        """
        # Si el jugador que captura es blanco, añade la pieza a la lista de capturas negras.
        if player_color == 'white':
            self.__captured_pieces_black__.append(piece)  # Añade la pieza capturada a la lista de piezas negras capturadas.
        else:
            self.__captured_pieces_white__.append(piece)  # Añade la pieza capturada a la lista de piezas blancas capturadas.

        # Mostrar mensaje en la consola indicando qué pieza fue capturada.
        print(f"¡{piece.__color__.capitalize()} {piece.__class__.__name__} ha sido capturada!")  # Muestra el color y el tipo de la pieza capturada.


    # ===== Retorna las piezas capturadas por el jugador contrario. =====
    def get_captured_pieces(self, player_color):
        """
        Parámetros:
        - player_color: el color del jugador que está pidiendo las piezas capturadas.
        Retorna:
        - Una lista con las piezas capturadas por el jugador contrario.
        """
        if player_color == 'white':  # Si el jugador es blanco, retorna las piezas negras capturadas.
            return self.__captured_pieces_black__
        else:  # Si el jugador es negro, retorna las piezas blancas capturadas.
            return self.__captured_pieces_white__


    # ===== Convierte una posición en notación de ajedrez (como 'e2') a coordenadas de matriz. =====
    def parse_position(self, position):
        """
        Parámetros:
        - position: la posición en notación de ajedrez.
        Retorna:
        - Un par (fila, columna) correspondiente a la matriz del tablero.
        """
        col = ord(position[0].lower()) - ord('a')  # Convierte la columna ('a'-'h') a un índice (0-7).
        row = 8 - int(position[1])  # Convierte la fila ('1'-'8') a un índice (0-7).
        return row, col  # Retorna las coordenadas (fila, columna).