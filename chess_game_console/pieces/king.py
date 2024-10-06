# pieces/king.py

from pieces.piece import Piece

# ===== Clase para la pieza del Rey. =====
class King(Piece):
    def symbol(self):
        # Símbolo 'K' para Rey blanco y 'k' para Rey negro
        return 'K' if self.__color__ == 'white' else 'k'

    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        # El Rey se mueve una casilla en cualquier dirección
        __row_diff__ = abs(__end_row__ - __start_row__)
        __col_diff__ = abs(__end_col__ - __start_col__)
        return (__row_diff__ <= 1 and __col_diff__ <= 1)

    # ===== Nuevo método para verificar si el Rey ha sido capturado =====
    def captured(self):
        print(f"¡El Rey {self.__color__} ha sido capturado! Fin del juego.")  # Mensaje de que el Rey ha sido capturado.
        exit()  # Termina el juego inmediatamente.
