# pieces/queen.py
from pieces.piece import Piece

# ===== Clase para la pieza de la Reina. =====
class Queen(Piece):
    def symbol(self):
        # Símbolo 'Q' para Reina blanca y 'q' para Reina negra
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # Diferencias de filas y columnas
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Verifica si el destino es válido
        if not self._is_destination_valid(end_row, end_col, board):
            return False

        # Verifica si el movimiento es horizontal, vertical o diagonal y si el camino está despejado
        if self._is_horizontal_move(row_diff, col_diff):
            return self._is_clear_horizontal_path(start_row, start_col, end_col, board)
        elif self._is_vertical_move(row_diff, col_diff):
            return self._is_clear_vertical_path(start_row, end_row, start_col, board)
        elif self._is_diagonal_move(row_diff, col_diff):
            return self._is_clear_diagonal_path(start_row, start_col, end_row, end_col, board)

        return False

    def _is_destination_valid(self, end_row, end_col, board):
        return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

    def _is_horizontal_move(self, row_diff, col_diff):
        return row_diff == 0 and col_diff > 0

    def _is_vertical_move(self, row_diff, col_diff):
        return col_diff == 0 and row_diff > 0

    def _is_diagonal_move(self, row_diff, col_diff):
        return row_diff == col_diff

    # Métodos específicos para limpiar cada tipo de camino
    def _is_clear_horizontal_path(self, start_row, start_col, end_col, board):
        return self._is_clear_path(start_row, start_col, 0, end_col, board, col_step=1 if end_col > start_col else -1)

    def _is_clear_vertical_path(self, start_row, end_row, start_col, board):
        return self._is_clear_path(start_row, start_col, end_row, 0, board, row_step=1 if end_row > start_row else -1)

    def _is_clear_diagonal_path(self, start_row, start_col, end_row, end_col, board):
        row_step = 1 if end_row > start_row else -1
        col_step = 1 if end_col > start_col else -1
        return self._is_clear_path(start_row, start_col, end_row, end_col, board, row_step, col_step)

    # Método genérico para verificar si el camino está despejado
    def _is_clear_path(self, start_row, start_col, end_row, end_col, board, row_step=0, col_step=0):
        row, col = start_row + row_step, start_col + col_step
        while row != end_row or col != end_col:
            if board[row][col] is not None:
                return False
            row += row_step
            col += col_step
        return True