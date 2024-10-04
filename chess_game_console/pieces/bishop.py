# pieces/bishop.py

from pieces.piece import Piece

class Bishop(Piece):
    def symbol(self):
        """
        Retorna el símbolo 'B' para el Alfil blanco y 'b' para el Alfil negro.
        """
        return 'B' if self.color == 'white' else 'b'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si un movimiento es válido para el Alfil.
        El movimiento es válido si:
        - El destino está dentro del tablero.
        - Es un movimiento diagonal.
        - El camino está despejado.
        """
        if not self._is_within_board(start_row, start_col, end_row, end_col):
            return False
        if not self._is_diagonal_move(start_row, start_col, end_row, end_col):
            return False
        
        step = (1 if end_row > start_row else -1, 1 if end_col > start_col else -1)
        return self.is_clear_path((start_row, start_col), (end_row, end_col), board, step)

    def _is_diagonal_move(self, start_row, start_col, end_row, end_col):
        """
        Verifica si el movimiento es diagonal. 
        Un movimiento es diagonal si la diferencia entre las filas es igual a la diferencia entre las columnas.
        """
        return abs(end_row - start_row) == abs(end_col - start_col)
