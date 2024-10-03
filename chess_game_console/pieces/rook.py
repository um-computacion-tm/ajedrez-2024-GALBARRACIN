# pieces/rook.py
from pieces.piece import Piece


# ===== Clase para la pieza de la torre. =====
class Rook(Piece):
    def symbol(self):
        return 'R' if self.color == 'white' else 'r'


    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        # Verificar si el movimiento es en línea recta
        if not self._is_straight_line_move(start_row, start_col, end_row, end_col):
            return False


        # Verificar si el camino está despejado
        if not self._is_path_clear(start_row, start_col, end_row, end_col, board):
            return False


        return True


    def _is_straight_line_move(self, start_row, start_col, end_row, end_col):
        """Verifica si el movimiento es en línea recta horizontal o vertical."""
        return start_row == end_row or start_col == end_col


    def _is_path_clear(self, start_row, start_col, end_row, end_col, board):
        """Verifica si hay piezas en el camino, ya sea en movimiento horizontal o vertical."""
        if start_row == end_row:  # Movimiento horizontal
            step = 1 if start_col < end_col else -1
            return self._check_path(start_row, start_col + step, end_col, step, board, is_vertical=False)
        elif start_col == end_col:  # Movimiento vertical
            step = 1 if start_row < end_row else -1
            return self._check_path(start_col, start_row + step, end_row, step, board, is_vertical=True)


    def _check_path(self, static_pos, step_start, step_end, step, board, is_vertical):
        """Verifica si el camino está libre de piezas, ya sea vertical o horizontal."""
        for pos in range(step_start, step_end, step):
            if is_vertical:
                if board[pos][static_pos] is not None:  # Revisamos en la columna estática
                    return False
            else:
                if board[static_pos][pos] is not None:  # Revisamos en la fila estática
                    return False
        return True