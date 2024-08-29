# pieces/piece.py
class Piece:
    """
    Clase base para todas las piezas del ajedrez.
    """
    def __init__(self, color):
        # Color de la pieza (blanco o negro)
        self.color = color

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Determina si el movimiento es válido (debe ser implementado por subclases).
        """
        raise NotImplementedError()

    def symbol(self):
        """
        Devuelve el símbolo que representa la pieza.
        """
        raise NotImplementedError()
