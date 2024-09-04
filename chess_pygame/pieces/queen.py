from pieces.bishop import check_bishop
from pieces.rook import check_rook

# ===== comprobar movimientos válidos de la reina =====
def check_queen(position, color):
    moves_list = check_bishop(position, color)  # Llama a la función check_bishop para obtener los movimientos válidos de un alfil desde la posición dada y los almacena en moves_list.
    second_list = check_rook(position, color)  # Llama a la función check_rook para obtener los movimientos válidos de una torre desde la posición dada y los almacena en second_list.
    for i in range(len(second_list)):  # Itera a través de todos los movimientos válidos obtenidos de la función check_rook. (Iteración significa repetir varias veces)
        moves_list.append(second_list[i])  # Añade cada movimiento válido de la torre a la lista de movimientos válidos de la reina (moves_list).
    return moves_list  # Devuelve la lista completa de movimientos válidos para la reina, combinando los movimientos de la torre y el alfil.
