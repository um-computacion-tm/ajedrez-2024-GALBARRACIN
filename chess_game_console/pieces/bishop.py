# pieces/bishop.py

from pieces.piece import Piece  # Importa la clase base Piece

# ===== Clase para la pieza del Alfil =====
class Bishop(Piece):
    def symbol(self):
        """
        Retorna el símbolo 'B' para el alfil blanco y 'b' para el alfil negro.
        """
        return 'B' if self.color == 'white' else 'b'  # Devuelve 'B' si es blanco, 'b' si es negro

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si un movimiento es válido para el Alfil.
        El movimiento es válido si:
        - Las posiciones están dentro del tablero.
        - Es un movimiento diagonal.
        - El camino está despejado (sin piezas bloqueando).
        """
        if not self._is_within_board(start_row, start_col, end_row, end_col):  # Verifica que las posiciones estén dentro del tablero
            return False
        if not self._is_diagonal_move(start_row, start_col, end_row, end_col):  # Verifica que sea un movimiento diagonal
            return False
        step = (1 if end_row > start_row else -1, 1 if end_col > start_col else -1)  # Calcula los pasos para moverse diagonalmente
        return self.is_clear_path((start_row, start_col), (end_row, end_col), board, step)  # Verifica si el camino está despejado utilizando el método común de Piece

    def _is_within_board(self, start_row, start_col, end_row, end_col):
        """
        Verifica si las posiciones de inicio y fin están dentro de los límites del tablero.
        """
        return all(0 <= pos < 8 for pos in [start_row, start_col, end_row, end_col])  # Se asegura de que todas las posiciones estén dentro de un tablero de 8x8

    def _is_diagonal_move(self, start_row, start_col, end_row, end_col):
        """
        Verifica si el movimiento es diagonal.
        Un movimiento es diagonal si la diferencia absoluta entre filas y columnas es la misma.
        """
        return abs(end_row - start_row) == abs(end_col - start_col)  # Retorna True si es movimiento diagonal
    