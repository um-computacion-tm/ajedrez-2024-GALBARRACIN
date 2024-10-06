# pieces/rook.py

from pieces.piece import Piece  # Importa la clase base Piece desde el módulo pieces.piece

# ===== Clase para la pieza de la torre (Rook) =====
class Rook(Piece):  # Define la clase Rook que hereda de Piece
    # ===== Retorna el símbolo de la Torre =====
    def symbol(self):  # Método para obtener el símbolo de la Torre
        return 'R' if self.__color__ == '__white__' else 'r'  # Retorna 'R' si es blanca, 'r' si es negra

    # ===== Verifica si un movimiento es válido para la Torre =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        # Verifica si el movimiento es en línea recta (horizontal o vertical)
        if not self._is_straight_line_move(__start_row__, __start_col__, __end_row__, __end_col__):
            return False  # Si no es en línea recta, el movimiento no es válido

        # Verifica si el camino entre el inicio y el destino está despejado
        if not self._is_path_clear(__start_row__, __start_col__, __end_row__, __end_col__, __board__):
            return False  # Si el camino no está despejado, el movimiento no es válido

        return True  # Si pasa las verificaciones, el movimiento es válido

    # ===== Verifica si el movimiento es en línea recta =====
    def _is_straight_line_move(self, __start_row__, __start_col__, __end_row__, __end_col__):
        """Verifica si el movimiento es en línea recta horizontal o vertical."""
        # Un movimiento es en línea recta si las filas o las columnas son iguales
        return __start_row__ == __end_row__ or __start_col__ == __end_col__

    # ===== Verifica si el camino está despejado =====
    def _is_path_clear(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        """Verifica si hay piezas en el camino, ya sea en movimiento horizontal o vertical."""
        if __start_row__ == __end_row__:  # Si el movimiento es horizontal
            # Verifica el camino en una fila fija (movimiento horizontal)
            return self._check_path(__start_row__, __start_col__, __end_col__, __board__, __is_vertical__=False)
        elif __start_col__ == __end_col__:  # Si el movimiento es vertical
            # Verifica el camino en una columna fija (movimiento vertical)
            return self._check_path(__start_col__, __start_row__, __end_row__, __board__, __is_vertical__=True)
        return False  # Si no es ni horizontal ni vertical, retorna False

    # ===== Verifica si el camino entre dos puntos está libre de piezas =====
    def _check_path(self, __static_pos__, __step_start__, __step_end__, __board__, __is_vertical__):
        """Verifica si el camino está libre de piezas, ya sea vertical o horizontal."""
        __step__ = 1 if __step_start__ < __step_end__ else -1  # Define el paso (dirección de movimiento)
        # Itera sobre las posiciones entre el inicio y el destino
        for __pos__ in range(__step_start__ + __step__, __step_end__, __step__):
            # Verifica si la posición está ocupada
            if self._is_occupied(__static_pos__, __pos__, __board__, __is_vertical__):
                return False  # Si está ocupada, el camino no está despejado
        return True  # Si no hay piezas en el camino, retorna True

    # ===== Verifica si una posición está ocupada por una pieza =====
    def _is_occupied(self, __static_pos__, __dynamic_pos__, __board__, __is_vertical__):
        """Verifica si una posición está ocupada por otra pieza."""
        if __is_vertical__:
            # Si el movimiento es vertical, revisa la columna estática y la fila dinámica
            return __board__[__dynamic_pos__][__static_pos__] is not None
        else:
            # Si el movimiento es horizontal, revisa la fila estática y la columna dinámica
            return __board__[__static_pos__][__dynamic_pos__] is not None

