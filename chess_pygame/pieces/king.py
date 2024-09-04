from board.board import black_locations, white_locations

# ===== comprobar movimientos válidos del rey =====
def check_king(position, color):
    moves_list = []  # Inicializa una lista vacía para almacenar los movimientos válidos del rey.   
    if color == 'white':  # Si el rey es blanco...
        enemies_list = black_locations  # ...los enemigos son las piezas negras.
        friends_list = white_locations  # ...los amigos son las piezas blancas.
    else:  # Si el rey es negro...
        friends_list = black_locations  # ...los amigos son las piezas negras.
        enemies_list = white_locations  # ...los enemigos son las piezas blancas.
    
    # 8 casillas para comprobar si hay reyes, pueden ir una casilla en cualquier dirección
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]  # Define las direcciones posibles a las que el rey puede moverse.
    for i in range(8):  # Itera a través de las 8 posibles direcciones.
        target = (position[0] + targets[i][0], position[1] + targets[i][1])  # Calcula la posición del movimiento potencial del rey.
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7: # Verifica que el movimiento esté dentro de los límites del tablero y no ocupe una casilla amiga.
            moves_list.append(target)  # Si el movimiento es válido, lo añade a la lista de movimientos. 
    return moves_list  # Devuelve la lista de movimientos válidos para el rey.
