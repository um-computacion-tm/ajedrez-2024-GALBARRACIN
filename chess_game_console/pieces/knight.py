# pieces/knight.py

from pieces.piece import Piece  # Importa la clase base Piece

# ===== Clase para la pieza del Caballo =====
class Knight(Piece):  # Define la clase Knight que hereda de Piece
    # ===== Retorna el símbolo del Caballo =====
    def symbol(self):
        # Retorna 'N' si el Caballo es blanco, 'n' si es negro
        return 'N' if self.__color__ == '__white__' else 'n'

    # ===== Verifica si el movimiento del Caballo es válido =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        """
        Verifica si el movimiento es válido para el Caballo.
        El Caballo se mueve en forma de 'L', lo que significa que la diferencia entre las filas
        y columnas debe ser de 2x1 o 1x2.
        """
        __row_diff__ = abs(__end_row__ - __start_row__)  # Calcula la diferencia entre las filas
        __col_diff__ = abs(__end_col__ - __start_col__)  # Calcula la diferencia entre las columnas
        
        # Verifica si el movimiento sigue el patrón 'L': 2x1 o 1x2
        return (__row_diff__ == 2 and __col_diff__ == 1) or (__row_diff__ == 1 and __col_diff__ == 2)
