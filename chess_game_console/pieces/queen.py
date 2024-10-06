# pieces/queen.py

from pieces.piece import Piece  # Importa la clase base Piece desde el módulo pieces.piece

# ===== Clase para la pieza de la Reina =====
class Queen(Piece):  # Define la clase Queen que hereda de Piece
    # ===== Retorna el símbolo de la Reina =====
    def symbol(self):  # Método para obtener el símbolo de la Reina
        """
        Retorna el símbolo 'Q' para la Reina blanca y 'q' para la Reina negra.
        """
        return 'Q' if self.__color__ == '__white__' else 'q'  # Retorna 'Q' si es blanca, 'q' si es negra

    # ===== Verifica si un movimiento es válido para la Reina =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        """
        Verifica si un movimiento es válido para la Reina.
        El movimiento es válido si:
        - El destino está dentro del tablero.
        - Es un movimiento válido (horizontal, vertical o diagonal).
        - El camino está despejado.
        - No está intentando capturar una pieza del mismo color.
        """
        # Verifica si las posiciones de inicio y fin están dentro del tablero
        if not self._is_within_board(__start_row__, __start_col__, __end_row__, __end_col__):
            return False  # Si no están dentro del tablero, el movimiento no es válido

        # Verificar si la casilla de destino contiene una pieza del mismo color
        __destination_piece__ = __board__[__end_row__][__end_col__]  # Obtiene la pieza en la posición de destino
        if __destination_piece__ is not None and __destination_piece__.__color__ == self.__color__:
            return False  # Si la pieza es del mismo color, no se puede capturar, movimiento inválido

        # Obtiene el tipo de movimiento (diagonal, horizontal o vertical)
        __move_type__ = self._get_move_type(__start_row__, __start_col__, __end_row__, __end_col__)
        if __move_type__ is None:
            return False  # Si el movimiento no es válido, retorna False

        # Calcula los pasos (incrementos) necesarios para moverse en la dirección adecuada
        __step__ = self._get_steps(__move_type__, __start_row__, __start_col__, __end_row__, __end_col__)
        # Verifica si el camino hacia el destino está despejado
        return self.is_clear_path((__start_row__, __start_col__), (__end_row__, __end_col__), __board__, __step__)

    # ===== Determina el tipo de movimiento =====
    def _get_move_type(self, __start_row__, __start_col__, __end_row__, __end_col__):
        """
        Determina el tipo de movimiento basado en las diferencias de filas y columnas.
        Retorna 'diagonal', 'horizontal' o 'vertical' según el movimiento, o None si no es válido.
        """
        # Calcula las diferencias absolutas entre las filas y las columnas
        __row_diff__, __col_diff__ = abs(__end_row__ - __start_row__), abs(__end_col__ - __start_col__)
        if __row_diff__ == __col_diff__:
            return 'diagonal'  # Movimiento en diagonal si las diferencias son iguales
        elif __row_diff__ == 0:
            return 'horizontal'  # Movimiento horizontal si las filas no cambian
        elif __col_diff__ == 0:
            return 'vertical'  # Movimiento vertical si las columnas no cambian
        return None  # Retorna None si el movimiento no es válido

    # ===== Calcula los pasos (incrementos) para el movimiento =====
    def _get_steps(self, __move_type__, __start_row__, __start_col__, __end_row__, __end_col__):
        """
        Calcula los pasos (incrementos) para las filas y columnas según el tipo de movimiento.
        """
        # Movimiento horizontal
        if __move_type__ == 'horizontal':
            return 0, 1 if __end_col__ > __start_col__ else -1  # Avanza 1 columna hacia la derecha o izquierda
        # Movimiento vertical
        elif __move_type__ == 'vertical':
            return 1 if __end_row__ > __start_row__ else -1, 0  # Avanza 1 fila hacia arriba o hacia abajo
        # Movimiento diagonal
        elif __move_type__ == 'diagonal':
            return 1 if __end_row__ > __start_row__ else -1, 1 if __end_col__ > __start_col__ else -1  # Avanza en ambas direcciones diagonalmente
