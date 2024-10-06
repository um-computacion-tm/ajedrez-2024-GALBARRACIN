# pieces/piece.py

# ===== Clase base para todas las piezas de ajedrez =====
class Piece:  # Define la clase base Piece
    # ===== Inicializa una pieza con un color =====
    def __init__(self, __color__):  # Constructor que inicializa la pieza con un color
        """
        Inicializa una pieza de ajedrez con el color dado.
        """
        self.__color__ = __color__  # Asigna el color de la pieza (blanco o negro)

    # ===== Verifica si un movimiento es válido (a ser implementado por subclases) =====
    def is_valid_move(self, __start_row__, __start_col__, __end_row__, __end_col__, __board__):
        """
        Método que debe ser implementado por las subclases para verificar si un movimiento es válido.
        """
        # Lanza una excepción si el método no es implementado por una subclase
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    # ===== Retorna el símbolo de la pieza (a ser implementado por subclases) =====
    def symbol(self):  # Método abstracto para retornar el símbolo de la pieza
        """
        Método que debe ser implementado por las subclases para retornar el símbolo de la pieza.
        """
        # Lanza una excepción si el método no es implementado por una subclase
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    # ===== Verifica si las posiciones están dentro del tablero =====
    def _is_within_board(self, __start_row__, __start_col__, __end_row__, __end_col__):  
        """
        Verifica si las posiciones de inicio y fin están dentro de los límites del tablero.
        """
        # Verifica que todas las posiciones estén dentro de los límites del tablero (0 a 7)
        return all(0 <= pos < 8 for pos in [__start_row__, __start_col__, __end_row__, __end_col__])

    # ===== Verifica si el camino entre dos posiciones está despejado =====
    def is_clear_path(self, __start__, __end__, __board__, __step__):
        """
        Verifica si el camino entre las posiciones 'start' y 'end' está despejado en el tablero.
        """
        # Calcula la primera posición después del inicio, moviéndose en la dirección del paso
        __current_row__, __current_col__ = __start__[0] + __step__[0], __start__[1] + __step__[1]

        # Recorre las posiciones hasta llegar a la posición de destino
        while (__current_row__, __current_col__) != __end__:
            # Si encuentra una pieza en el camino, retorna False
            if __board__[__current_row__][__current_col__] is not None:
                return False
            # Avanza a la siguiente posición según el paso definido
            __current_row__ += __step__[0]
            __current_col__ += __step__[1]

        return True  # Si no encuentra piezas en el camino, retorna True

