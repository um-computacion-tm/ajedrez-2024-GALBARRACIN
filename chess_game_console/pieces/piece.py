# pieces/piece.py

# ===== Clase base para todas las piezas del ajedrez =====
class Piece:
    def __init__(self, color):
        # Color de la pieza (blanco o negro)
        self.color = color

    # ===== Determina si el movimiento es válido ======
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Verifica si el movimiento es válido para la pieza.
        Este método debe ser implementado por las clases hijas (piezas específicas).
        """
        raise NotImplementedError("Este método debe ser implementado en las piezas específicas.")

    # ===== Devuelve el símbolo que representa la pieza =====
    def symbol(self):
        """
        Devuelve el símbolo que representa la pieza.
        Este método debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("Este método debe ser implementado en las piezas específicas.")

    # ===== Verifica si el camino entre dos puntos está despejado =====
    def is_clear_path(self, start_pos, end_pos, board, step):
        """
        Verifica si el camino entre dos posiciones está despejado.
        Se mueve desde start_pos hasta end_pos en pasos definidos por `step`.
        - start_pos: tupla (fila, columna) de la posición inicial.
        - end_pos: tupla (fila, columna) de la posición final.
        - board: el tablero de ajedrez.
        - step: tupla (row_step, col_step) que indica la dirección del movimiento.
        """
        current_row, current_col = start_pos
        end_row, end_col = end_pos
        row_step, col_step = step

        # Mueve desde la posición inicial a la final, verificando si hay obstáculos en el camino
        current_row += row_step
        current_col += col_step

        while (current_row, current_col) != (end_row, end_col):
            if board[current_row][current_col] is not None:  # Si hay una pieza en el camino, movimiento inválido
                return False
            current_row += row_step
            current_col += col_step
        
        return True  # El camino está despejado
