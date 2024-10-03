# pieces/queen.py
from pieces.piece import Piece

# ===== Clase para la pieza de la Reina =====
class Queen(Piece):
    def symbol(self):
        # Símbolo 'Q' para Reina blanca y 'q' para Reina negra
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Verifica si el destino es válido
        if not self._is_destination_valid(end_row, end_col, board):
            return False

        # Determina el tipo de movimiento
        move_type = self._get_move_type(row_diff, col_diff)

        # Verifica si el movimiento es válido y si el camino está despejado
        return move_type is not None and move_type(start_row, start_col, end_row, end_col, board)

    def _get_move_type(self, row_diff, col_diff):
        if self._is_horizontal_move(row_diff, col_diff):
            return self._is_clear_horizontal_path
        elif self._is_vertical_move(row_diff, col_diff):
            return self._is_clear_vertical_path
        elif self._is_diagonal_move(row_diff, col_diff):
            return self._is_clear_diagonal_path
        return None

    def _is_destination_valid(self, end_row, end_col, board):
        destination_piece = board[end_row][end_col]
        return destination_piece is None or destination_piece.color != self.color

    def _is_horizontal_move(self, row_diff, col_diff):
        return row_diff == 0 and col_diff > 0

    def _is_vertical_move(self, row_diff, col_diff):
        return col_diff == 0 and row_diff > 0

    def _is_diagonal_move(self, row_diff, col_diff):
        return row_diff == col_diff

    def _is_clear_horizontal_path(self, start_row, start_col, end_row, end_col, board):
        col_step = 1 if end_col > start_col else -1
        return self._is_clear_linear_path(start_row, start_col, end_row, end_col, board, row_step=0, col_step=col_step)

    def _is_clear_vertical_path(self, start_row, start_col, end_row, end_col, board):
        row_step = 1 if end_row > start_row else -1
        return self._is_clear_linear_path(start_row, start_col, end_row, end_col, board, row_step=row_step, col_step=0)

    def _is_clear_diagonal_path(self, start_row, start_col, end_row, end_col, board):
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        return self._is_clear_linear_path(start_row, start_col, end_row, end_col, board, row_step=row_step, col_step=col_step)

    # Método genérico para verificar si el camino está despejado en línea recta
    def _is_clear_linear_path(self, start_row, start_col, end_row, end_col, board, row_step, col_step):
        row, col = start_row + row_step, start_col + col_step
        while row != end_row or col != end_col:
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step
        return True