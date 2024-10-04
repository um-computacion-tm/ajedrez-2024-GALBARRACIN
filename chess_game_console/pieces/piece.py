# pieces/piece.py

class Piece:
    def __init__(self, color):
        """
        Inicializa una pieza de ajedrez con el color dado.
        """
        self.color = color

    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        """
        Método que debe ser implementado por las subclases para verificar si un movimiento es válido.
        """
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def symbol(self):
        """
        Método que debe ser implementado por las subclases para retornar el símbolo de la pieza.
        """
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def _is_within_board(self, start_row, start_col, end_row, end_col):
        """
        Verifica si las posiciones de inicio y fin están dentro de los límites del tablero.
        """
        return all(0 <= pos < 8 for pos in [start_row, start_col, end_row, end_col])

    def is_clear_path(self, start, end, board, step):
        """
        Verifica si el camino entre las posiciones 'start' y 'end' está despejado en el tablero.
        """
        current_row, current_col = start[0] + step[0], start[1] + step[1]

        while (current_row, current_col) != end:
            if board[current_row][current_col] is not None:
                return False
            current_row += step[0]
            current_col += step[1]

        return True
