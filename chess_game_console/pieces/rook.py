# pieces/rook.py
from pieces.piece import Piece

# ===== Clase para la pieza de la torre. =====
class Rook(Piece):
    def symbol(self):
        return 'R' if self.color == 'white' else 'r'

    # ===== Verifica si el movimiento de la torre es válido. La torre puede moverse en línea recta horizontalmente o verticalmente. =====
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if start_row != end_row and start_col != end_col:
            # Movimiento no válido: la torre no se mueve en diagonal
            return False

        # Determinar la dirección del movimiento
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            # Verificar si hay piezas en el camino horizontalmente
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
        elif start_col == end_col:  # Movimiento vertical
            step = 1 if start_row < end_row else -1
            # Verificar si hay piezas en el camino verticalmente
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
        else:
            return False  # Esto maneja cualquier movimiento no recto

        # Si pasa todas las verificaciones, el movimiento es válido
        return True
