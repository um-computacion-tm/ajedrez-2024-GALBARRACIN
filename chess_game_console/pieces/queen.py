# pieces/queen.py
from pieces.piece import Piece  # Importa la clase base Piece

# ===== Clase para la pieza de la Reina =====
class Queen(Piece):
    def symbol(self):
        """
        Retorna el símbolo 'Q' para la Reina blanca y 'q' para la Reina negra.
        """
        return 'Q' if self.color == 'white' else 'q'  # Devuelve el símbolo dependiendo del color de la pieza

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si un movimiento es válido para la Reina.
        El movimiento es válido si:
        - El destino es válido (no hay piezas del mismo color).
        - Es un movimiento válido (horizontal, vertical o diagonal).
        - El camino está despejado.
        """
        if not self._is_within_board(start_row, start_col, end_row, end_col):
            return False

        if not self._is_destination_valid(end_row, end_col, board):  # Verifica si el destino es válido
            return False

        move_type = self._get_move_type(start_row, start_col, end_row, end_col)  # Obtiene el tipo de movimiento
        return move_type and self._is_path_clear(((start_row, start_col), (end_row, end_col)), board, move_type)
        # Verifica que el tipo de movimiento sea válido y que el camino esté despejado

    def _is_within_board(self, start_row, start_col, end_row, end_col):
        """
        Verifica si las posiciones de inicio y fin están dentro de los límites del tablero.
        """
        return all(0 <= pos < 8 for pos in [start_row, start_col, end_row, end_col])

    def _get_move_type(self, start_row, start_col, end_row, end_col):
        """
        Determina el tipo de movimiento basado en las diferencias de filas y columnas.
        Retorna 'diagonal', 'horizontal' o 'vertical' según el movimiento, o None si no es válido.
        """
        row_diff, col_diff = abs(end_row - start_row), abs(end_col - start_col)  # Calcula la diferencia de filas y columnas
        if row_diff == col_diff:  # Movimiento diagonal
            return 'diagonal'
        elif row_diff == 0:  # Movimiento horizontal
            return 'horizontal'
        elif col_diff == 0:  # Movimiento vertical
            return 'vertical'
        return None  # Si no cumple ninguna condición, no es un movimiento válido

    def _is_destination_valid(self, end_row, end_col, board):
        """
        Verifica si el destino es válido, es decir, si no hay una pieza del mismo color en la posición de destino.
        """
        destination_piece = board[end_row][end_col]  # Obtiene la pieza en el destino
        return destination_piece is None or destination_piece.color != self.color
        # El destino es válido si no hay pieza o si es de otro color

    def _is_path_clear(self, positions, board, move_type):
        """
        Verifica si el camino está despejado para el tipo de movimiento (horizontal, vertical o diagonal).
        Utiliza una tupla 'positions' que contiene las coordenadas de inicio y fin.
        """
        start, end = positions  # Desempaqueta las posiciones de inicio y fin
        step = self._get_steps(start, end, move_type)  # Obtiene los pasos (incrementos) según el tipo de movimiento
        return self.is_clear_path(start, end, board, step)  # Usa el método común de Piece para verificar si el camino está despejado

    def _get_steps(self, start, end, move_type):
        """
        Calcula los pasos (incrementos) para las filas y columnas según el tipo de movimiento.
        """
        start_row, start_col = start  # Desempaqueta la posición de inicio
        end_row, end_col = end  # Desempaqueta la posición de fin

        if move_type == 'horizontal':  # Si es movimiento horizontal
            return 0, 1 if end_col > start_col else -1  # Columna se mueve, fila se mantiene
        elif move_type == 'vertical':  # Si es movimiento vertical
            return 1 if end_row > start_row else -1, 0  # Fila se mueve, columna se mantiene
        elif move_type == 'diagonal':  # Si es movimiento diagonal
            return 1 if end_row > start_row else -1, 1 if end_col > start_col else -1  # Tanto fila como columna se mueven en diagonal