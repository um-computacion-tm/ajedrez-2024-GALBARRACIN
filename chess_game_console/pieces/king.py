# pieces/king.py
from pieces.piece import Piece

class King(Piece):
    """
    Clase para la pieza del Rey.
    """
    def symbol(self):
        # Símbolo 'K' para Rey blanco y 'k' para Rey negro
        return 'K' if self.color == 'white' else 'k'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # El Rey se mueve una casilla en cualquier dirección
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return (row_diff <= 1 and col_diff <= 1)
