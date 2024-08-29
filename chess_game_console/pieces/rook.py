# pieces/rook.py
from pieces.piece import Piece

class Rook(Piece):
    """
    Clase para la pieza de la torre.
    """
    def symbol(self):
        return 'R' if self.color == 'white' else 'r'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # Lógica de validación del movimiento de la torre
        return True  # Simplificado
