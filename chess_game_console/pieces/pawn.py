# pieces/pawn.py
from pieces.piece import Piece

class Pawn(Piece):
    """
    Clase para la pieza del peón.
    """
    def symbol(self):
        return 'P' if self.color == 'white' else 'p'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # Lógica de validación del movimiento del peón
        direction = 1 if self.color == 'black' else -1
        if start_col == end_col:  # Movimiento vertical
            if (end_row - start_row) == direction:
                return board[end_row][end_col] is None
        # Otros movimientos válidos pueden ser agregados aquí (capturas, primer movimiento, etc.)
        return False
