# pieces/piece.py

# ===== Clase base para todas las piezas del ajedrez. =====
class Piece:
    def __init__(self, color):
        # Color de la pieza (blanco o negro)
        self.color = color

# ===== Determina si el movimiento es válido ======
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        raise NotImplementedError()
    
# ===== Devuelve el símbolo que representa la pieza. =====
    def symbol(self):
        raise NotImplementedError()

# Determina si el movimiento es válido (debe ser implementado por subclases).