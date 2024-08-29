# pieces/knight.py
from pieces.piece import Piece

class Knight(Piece):
    """
    Clase para la pieza del Caballo.
    """
    def symbol(self):
        # Símbolo 'N' para Caballo blanco y 'n' para Caballo negro
        return 'N' if self.color == 'white' else 'n'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # El Caballo se mueve en forma de 'L': 2x1 o 1x2
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
