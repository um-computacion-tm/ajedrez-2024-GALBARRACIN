# pieces/bishop.py

from pieces.piece import Piece

# ===== Clase para la pieza del Alfil. =====
class Bishop(Piece):

    def symbol(self):
        """
        Devuelve el símbolo que representa el alfil.
        'B' para alfil blanco y 'b' para alfil negro.
        """
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Determina si un movimiento es válido para el alfil.
        El alfil se mueve diagonalmente, por lo que el movimiento es válido
        si la diferencia absoluta entre las filas y columnas es la misma.
        Además, verifica que no haya piezas en el camino.
        """
        # Verificar límites del tablero
        if not (0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        # El alfil se mueve en diagonal: el movimiento es válido si la diferencia
        # absoluta entre filas y columnas es la misma.
        if abs(end_row - start_row) != abs(end_col - start_col):
            return False

        # Verificar que no haya piezas en el camino
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        current_row, current_col = start_row + row_step, start_col + col_step

        while current_row != end_row and current_col != end_col:
            if board[current_row][current_col] is not None:  # Si hay una pieza en el camino
                return False
            current_row += row_step
            current_col += col_step

        return True
