# pieces/bishop.py

# ===== Clase Alfil (Bishop) =====
from pieces.piece import Piece  # Importa la clase base Piece desde el módulo pieces.piece

# ===== Retorna el símbolo del Alfil =====
class Bishop(Piece):  # Define la clase Bishop que hereda de Piece
    def symbol(self):  # Método para obtener el símbolo del alfil
        """
        Retorna el símbolo 'B' para el Alfil blanco y 'b' para el Alfil negro.
        """
        return 'B' if self.__color__ == '__white__' else 'b'  # Retorna 'B' si es blanco, 'b' si es negro

    # ===== Verifica si un movimiento es válido para el Alfil =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        """
        Verifica si un movimiento es válido para el Alfil.
        El movimiento es válido si:
        - El destino está dentro del tablero.
        - Es un movimiento diagonal.
        - El camino está despejado.
        """
        if not self._is_within_board(__start_row__, __start_col__, __end_row__, __end_col__):  # Comprueba si las coordenadas están dentro del tablero
            return False  # Si no está dentro del tablero, retorna False
        if not self._is_diagonal_move(__start_row__, __start_col__, __end_row__, __end_col__):  # Verifica si el movimiento es diagonal
            return False  # Si no es un movimiento diagonal, retorna False
        
        # Calcula el paso para moverse diagonalmente en filas y columnas
        __step__ = (1 if __end_row__ > __start_row__ else -1, 1 if __end_col__ > __start_col__ else -1)  
        # Verifica si el camino está despejado
        return self.is_clear_path((__start_row__, __start_col__), (__end_row__, __end_col__), __board__, __step__)  

    # ===== Verifica si el movimiento es diagonal =====
    def _is_diagonal_move(self, __start_row__, __start_col__, __end_row__, __end_col__):
        """
        Verifica si el movimiento es diagonal. 
        Un movimiento es diagonal si la diferencia entre las filas es igual a la diferencia entre las columnas.
        """
        # Retorna True si la diferencia en filas es igual a la diferencia en columnas (movimiento diagonal)
        return abs(__end_row__ - __start_row__) == abs(__end_col__ - __start_col__)  

