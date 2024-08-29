# pieces/bishop.py
from pieces.piece import Piece

class Bishop(Piece):
    """
    Clase para la pieza del Alfil.
    """
    def symbol(self):
        # Símbolo 'B' para Alfil blanco y 'b' para Alfil negro
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # El Alfil se mueve diagonalmente: el movimiento es válido si la diferencia
        # absoluta entre filas y columnas es la misma
        return abs(end_row - start_row) == abs(end_col - start_col)
