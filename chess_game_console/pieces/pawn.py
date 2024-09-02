# pieces/pawn.py
from pieces.piece import Piece

# ===== Clase para la pieza del peón. =====
class Pawn(Piece):
    def symbol(self):
        return 'P' if self.color == 'white' else 'p'

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        direction = 1 if self.color == 'black' else -1
        start_row_expected = 1 if self.color == 'black' else 6

        # Movimiento hacia adelante (una casilla)
        if start_col == end_col:
            if (end_row - start_row) == direction and board[end_row][end_col] is None:
                return True
            # Movimiento de dos casillas hacia adelante en el primer movimiento
            if (start_row == start_row_expected and 
                (end_row - start_row) == 2 * direction and 
                board[start_row + direction][start_col] is None and 
                board[end_row][end_col] is None):
                return True
        
        # Captura en diagonal
        if abs(start_col - end_col) == 1 and (end_row - start_row) == direction:
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True

        return False
