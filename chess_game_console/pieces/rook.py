# pieces/rook.py
from pieces.piece import Piece


# ===== Clase para la pieza de la torre (Rook). =====
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
            return self._check_path(start_row, start_col, end_col, board, is_vertical=False)
        elif start_col == end_col:  # Movimiento vertical
            return self._check_path(start_col, start_row, end_row, board, is_vertical=True)
        return False

    def _check_path(self, static_pos, step_start, step_end, board, is_vertical):
        """Verifica si el camino está libre de piezas, ya sea vertical o horizontal."""
        step = 1 if step_start < step_end else -1
        for pos in range(step_start + step, step_end, step):
            if self._is_occupied(static_pos, pos, board, is_vertical):
                return False
        return True

    def _is_occupied(self, static_pos, dynamic_pos, board, is_vertical):
        """Verifica si una posición está ocupada por otra pieza."""
        if is_vertical:
            return board[dynamic_pos][static_pos] is not None  # Revisamos en la columna estática
        else:
            return board[static_pos][dynamic_pos] is not None  # Revisamos en la fila estática