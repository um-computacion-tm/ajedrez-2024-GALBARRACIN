# board/board.py
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King

class Board:
    """
    Representa el tablero de ajedrez.
    """
    def __init__(self):
        # Crea un tablero 8x8 con None en cada posición
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        # Posiciona las piezas iniciales en el tablero
        self.setup_board()

    def setup_board(self):
        """
        Configura el tablero con las piezas en las posiciones iniciales.
        """
        # Coloca los peones blancos y negros
        for i in range(8):
            self.grid[1][i] = Pawn('black')
            self.grid[6][i] = Pawn('white')

        # Coloca otras piezas
        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(placement):
            self.grid[0][i] = piece('black')
            self.grid[7][i] = piece('white')

    def display(self):
        """
        Muestra el tablero en la consola.
        """
        # Imprime las filas y columnas del tablero
        for row in self.grid:
            print(' '.join([piece.symbol() if piece else '.' for piece in row]))

    def move_piece(self, start, end, player_color):
        """
        Mueve una pieza de una posición a otra.
        """
        start_row, start_col = self.parse_position(start)
        end_row, end_col = self.parse_position(end)

        piece = self.grid[start_row][start_col]
        target = self.grid[end_row][end_col]

        if piece and piece.color == player_color:
            # Verifica si el movimiento es válido
            if piece.is_valid_move(start_row, start_col, end_row, end_col, self.grid):
                # Captura de pieza
                if target:
                    self.capture_piece(target)

                # Mueve la pieza en el tablero
                self.grid[end_row][end_col] = piece
                self.grid[start_row][start_col] = None
                return True
            else:
                print("Movimiento no válido para esa pieza.")
        else:
            print("No hay una pieza de tu color en la posición inicial.")
        return False

    def capture_piece(self, piece):
        """
        Maneja la captura de una pieza en el tablero.
        """
        # Este método podría usarse para hacer algo con las piezas capturadas
        pass

    def parse_position(self, position):
        """
        Convierte posiciones de notación de ajedrez a coordenadas de matriz.
        """
        col = ord(position[0].lower()) - ord('a')
        row = 8 - int(position[1])
        return row, col
