# pieces/pawn.py

from pieces.piece import Piece  # Importa la clase base Piece desde el módulo pieces.piece

# ===== Clase para la pieza del peón =====
class Pawn(Piece):  # Define la clase Pawn que hereda de Piece
    # ===== Retorna el símbolo del Peón =====
    def symbol(self):  # Método para obtener el símbolo del Peón
        return 'P' if self.__color__ == 'white' else 'p'  # Retorna 'P' si es blanco, 'p' si es negro

    # ===== Verifica si un movimiento es válido para el Peón =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        __direction__ = 1 if self.__color__ == 'black' else -1  # Define la dirección del movimiento: 1 hacia abajo (negro), -1 hacia arriba (blanco)
        __start_row_expected__ = 1 if self.__color__ == 'black' else 6  # Fila inicial esperada dependiendo del color del Peón

        # ===== Movimiento hacia adelante (una casilla) =====
        if __start_col__ == __end_col__:  # El movimiento recto ocurre si las columnas son iguales
            if (__end_row__ - __start_row__) == __direction__ and __board__[__end_row__][__end_col__] is None:  
                # El peón se mueve una casilla hacia adelante si está libre
                return True  # Movimiento válido hacia adelante
            
            # ===== Movimiento de dos casillas hacia adelante en el primer movimiento =====
            if (__start_row__ == __start_row_expected__ and  # Verifica si el peón está en su fila inicial
                (__end_row__ - __start_row__) == 2 * __direction__ and  # El peón puede avanzar dos casillas hacia adelante
                __board__[__start_row__ + __direction__][__start_col__] is None and  # Verifica que la casilla intermedia esté libre
                __board__[__end_row__][__end_col__] is None):  # Verifica que la casilla final esté libre
                return True  # Movimiento válido de dos casillas

        # ===== Captura en diagonal =====
        if abs(__start_col__ - __end_col__) == 1 and (__end_row__ - __start_row__) == __direction__:  
            # La captura en diagonal ocurre cuando el peón se mueve una casilla en diagonal
            if __board__[__end_row__][__end_col__] is not None and __board__[__end_row__][__end_col__].__color__ != self.__color__:  
                # Verifica si hay una pieza del oponente en la casilla de destino
                return True  # Movimiento válido de captura

        return False  # Si ninguna de las condiciones se cumple, el movimiento es inválido

