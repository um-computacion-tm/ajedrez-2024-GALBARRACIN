# pieces/queen.py

from pieces.piece import Piece

class Queen(Piece):
    def symbol(self):
        """
        Retorna el símbolo 'Q' para la Reina blanca y 'q' para la Reina negra.
        """
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si un movimiento es válido para la Reina.
        El movimiento es válido si:
        - El destino está dentro del tablero.
        - Es un movimiento válido (horizontal, vertical o diagonal).
        - El camino está despejado.
        - No está intentando capturar una pieza del mismo color.
        """
        if not self._is_within_board(start_row, start_col, end_row, end_col):
            return False

        # Verificar si la casilla de destino contiene una pieza del mismo color
        destination_piece = board[end_row][end_col]
        if destination_piece is not None and destination_piece.color == self.color:
            return False

        move_type = self._get_move_type(start_row, start_col, end_row, end_col)
        if move_type is None:
            return False

        step = self._get_steps(move_type, start_row, start_col, end_row, end_col)
        return self.is_clear_path((start_row, start_col), (end_row, end_col), board, step)

    def _get_move_type(self, start_row, start_col, end_row, end_col):
        """
        Determina el tipo de movimiento basado en las diferencias de filas y columnas.
        Retorna 'diagonal', 'horizontal' o 'vertical' según el movimiento, o None si no es válido.
        """
        row_diff, col_diff = abs(end_row - start_row), abs(end_col - start_col)
        if row_diff == col_diff:
            return 'diagonal'
        elif row_diff == 0:
            return 'horizontal'
        elif col_diff == 0:
            return 'vertical'
        return None

    def _get_steps(self, move_type, start_row, start_col, end_row, end_col):
        """
        Calcula los pasos (incrementos) para las filas y columnas según el tipo de movimiento.
        """
        if move_type == 'horizontal':
            return 0, 1 if end_col > start_col else -1
        elif move_type == 'vertical':
            return 1 if end_row > start_row else -1, 0
        elif move_type == 'diagonal':
            return 1 if end_row > start_row else -1, 1 if end_col > start_col else -1
