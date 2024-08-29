# pieces/queen.py
from pieces.piece import Piece

class Queen(Piece):
    """
    Clase para la pieza de la Reina.
    """
    def symbol(self):
        # Símbolo 'Q' para Reina blanca y 'q' para Reina negra
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # La Reina se mueve como una Torre o un Alfil
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return (row_diff == 0 or col_diff == 0) or (row_diff == col_diff)
