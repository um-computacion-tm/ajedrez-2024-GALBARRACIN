# board/board.py
from pieces.pawn import Pawn                    # Importa la clase Pawn para representar los peones.
from pieces.rook import Rook                    # Importa la clase Rook para representar las torres.
from pieces.knight import Knight                # Importa la clase Knight para representar los caballos.
from pieces.bishop import Bishop                # Importa la clase Bishop para representar los alfiles.
from pieces.queen import Queen                  # Importa la clase Queen para representar las reinas.
from pieces.king import King                    # Importa la clase King para representar los reyes.



# ===== Representa el tablero de ajedrez.=====
class Board:                                    # Define la clase Board que representa el tablero de ajedrez.
    
    def __init__(self):                         # Método constructor que inicializa un nuevo tablero.
        # Crea un tablero 8x8 con None en cada posición
        self.grid = [[None for _ in range(8)] for _ in range(8)]  # Inicializa una matriz 8x8 con None en todas las posiciones.
        # Posiciona las piezas iniciales en el tablero
        self.setup_board()                      # Llama al método setup_board() para colocar las piezas en sus posiciones iniciales.


# ===== Configura el tablero con las piezas en las posiciones iniciales.=====
    def setup_board(self):                      # Método que configura las piezas en el tablero.
        
        # Coloca los peones blancos y negros
        for i in range(8):                      # Itera sobre cada columna de la primera y sexta fila.
            self.grid[1][i] = Pawn('black')     # Coloca un peón negro en la fila 2 (índice 1).
            self.grid[6][i] = Pawn('white')     # Coloca un peón blanco en la fila 7 (índice 6).

        # Coloca otras piezas
        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]  # Define la secuencia de piezas en la primera y última fila.
        for i, piece in enumerate(placement):    # Itera sobre cada columna y pieza del arreglo placement.
            self.grid[0][i] = piece('black')     # Coloca las piezas negras en la fila 1 (índice 0).
            self.grid[7][i] = piece('white')     # Coloca las piezas blancas en la fila 8 (índice 7).


# ===== Muestra el tablero en la consola. =====
    def display(self):                           # Método que muestra el tablero en la consola.
    
        # Imprime las filas y columnas del tablero
        for row in self.grid:                    # Itera sobre cada fila del tablero.
            print(' '.join([piece.symbol() if piece else '.' for piece in row]))  # Imprime cada pieza o un punto si la posición está vacía.



# ===== Mueve una pieza de una posición a otra. =====
    def move_piece(self, start, end, player_color):  # Método que maneja el movimiento de una pieza en el tablero.
        
        start_row, start_col = self.parse_position(start)  # Convierte la posición inicial en coordenadas de la matriz.
        end_row, end_col = self.parse_position(end)        # Convierte la posición final en coordenadas de la matriz.

        piece = self.grid[start_row][start_col]            # Obtiene la pieza en la posición inicial.
        target = self.grid[end_row][end_col]               # Obtiene la pieza en la posición final (si hay alguna).

        if piece and piece.color == player_color:          # Verifica que haya una pieza del color correcto en la posición inicial.
            # Verifica si el movimiento es válido
            if piece.is_valid_move(start_row, start_col, end_row, end_col, self.grid):  # Comprueba si el movimiento es válido.
                # Captura de pieza
                if target:                                  # Si hay una pieza en la posición final, la captura.
                    self.capture_piece(target)              # Llama al método capture_piece() para manejar la captura.

                # Mueve la pieza en el tablero
                self.grid[end_row][end_col] = piece         # Coloca la pieza en la nueva posición.
                self.grid[start_row][start_col] = None      # Vacía la posición inicial.
                return True                                 # Retorna True indicando que el movimiento fue exitoso.
            else:
                print("Movimiento no válido para esa pieza.")  # Informa si el movimiento no es válido.
        else:
            print("No hay una pieza de tu color en la posición inicial.")  # Informa si no hay una pieza válida en la posición inicial.
        return False                                        # Retorna False si el movimiento no fue exitoso.


# ===== Maneja la captura de una pieza en el tablero. =====
    def capture_piece(self, piece):                         # Método  para manejar la captura de una pieza.
        
        # Este método podría usarse para hacer algo con las piezas capturadas
        pass                                                # Actualmente no hace nada, pero se puede expandir.

# ===== Convierte posiciones de notación de ajedrez a coordenadas de matriz. =====
    def parse_position(self, position):                     # Método que convierte una posición en notación de ajedrez a coordenadas de matriz.

        col = ord(position[0].lower()) - ord('a')           # Convierte la columna de notación ('a'-'h') a índice de matriz (0-7).
        row = 8 - int(position[1])                          # Convierte la fila de notación ('1'-'8') a índice de matriz (0-7).
        return row, col                                     # Retorna las coordenadas de la matriz (fila, columna).
