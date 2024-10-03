# pieces/bishop.py

from pieces.piece import Piece

class Bishop(Piece):

    def symbol(self):
        """
        Retorna 'B' para alfil blanco y 'b' para alfil negro.
        """
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si un movimiento es válido para el alfil. El alfil se mueve
        diagonalmente, por lo que el movimiento es válido si la diferencia 
        absoluta entre filas y columnas es la misma y no hay piezas en el camino.
        """
        if not self._is_within_board(start_row, start_col, end_row, end_col):
            return False
        
        if not self._is_diagonal_move(start_row, start_col, end_row, end_col):
            return False
        
        if self._is_path_blocked(start_row, start_col, end_row, end_col, board):
            return False
        
        return True

    def _is_within_board(self, start_row, start_col, end_row, end_col):
        """Verifica si las posiciones están dentro de los límites del tablero."""
        return all(0 <= pos < 8 for pos in [start_row, start_col, end_row, end_col])

    def _is_diagonal_move(self, start_row, start_col, end_row, end_col):
        """Verifica si el movimiento es diagonal."""
        return abs(end_row - start_row) == abs(end_col - start_col)

    def _is_path_blocked(self, start_row, start_col, end_row, end_col, board):
        """Verifica si hay piezas en el camino entre el punto de inicio y el punto final."""
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        current_row, current_col = start_row + row_step, start_col + col_step

        while current_row != end_row and current_col != end_col:
            if board[current_row][current_col] is not None:
                return True
            current_row += row_step
            current_col += col_step

        return False