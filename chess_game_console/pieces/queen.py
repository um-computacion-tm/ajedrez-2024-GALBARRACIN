# pieces/queen.py
from pieces.piece import Piece

# ===== Clase para la pieza de la Reina. =====
class Queen(Piece):
    def symbol(self):
        # Símbolo 'Q' para Reina blanca y 'q' para Reina negra
        return 'Q' if self.color == 'white' else 'q'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        # Movimiento horizontal
        if row_diff == 0:
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
            # Verifica que la pieza destino sea del mismo color
            return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

        # Movimiento vertical
        elif col_diff == 0:
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
            # Verifica que la pieza destino sea del mismo color
            return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

        # Movimiento diagonal
        elif row_diff == col_diff:
            row_step = 1 if end_row > start_row else -1
            col_step = 1 if end_col > start_col else -1
            row, col = start_row + row_step, start_col + col_step
            while row != end_row and col != end_col:
                if board[row][col] is not None:
                    return False
                row += row_step
                col += col_step
            # Verifica que la pieza destino sea del mismo color
            return board[end_row][end_col] is None or board[end_row][end_col].color != self.color

        return False
