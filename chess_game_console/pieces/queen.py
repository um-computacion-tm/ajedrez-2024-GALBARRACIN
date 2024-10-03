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


        # Verifica si el destino es válido y el movimiento es horizontal, vertical o diagonal
        valid_destination = self._is_destination_valid(end_row, end_col, board)
        if not valid_destination:
            return False
       
        valid_move = (
            (self._is_horizontal_move(row_diff, col_diff) and self._is_clear_path(start_row, start_col, end_row, end_col, board, "horizontal")) or
            (self._is_vertical_move(row_diff, col_diff) and self._is_clear_path(start_row, start_col, end_row, end_col, board, "vertical")) or
            (self._is_diagonal_move(row_diff, col_diff) and self._is_clear_path(start_row, start_col, end_row, end_col, board, "diagonal"))
        )
       
        return valid_move


    def _is_destination_valid(self, end_row, end_col, board):
        return (board[end_row][end_col] is None or board[end_row][end_col].color != self.color)


    def _is_horizontal_move(self, row_diff, col_diff):
        return row_diff == 0 and col_diff > 0


    def _is_vertical_move(self, row_diff, col_diff):
        return col_diff == 0 and row_diff > 0


    def _is_diagonal_move(self, row_diff, col_diff):
        return row_diff == col_diff


    # Refactorización de los tres métodos de validación de camino en uno solo
    def _is_clear_path(self, start_row, start_col, end_row, end_col, board, direction):
        if direction == "horizontal":
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False


        elif direction == "vertical":
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False


        elif direction == "diagonal":
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row and col != end_col:
                if board[row][col] is not None:
                    return False
                row += row_step
                col += col_step


        return True