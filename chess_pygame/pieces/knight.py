from board.board import black_locations, white_locations

# ===== comprobar movimientos válidos del caballo =====
def check_knight(position, color):  # Función para comprobar los movimientos posibles de un caballo
    moves_list = []  # Lista para almacenar los movimientos posibles del caballo

    # Determinar la lista de piezas enemigas y aliadas según el color del caballo
    if color == 'white':  # Si el caballo es blanco
        enemies_list = black_locations  # Las piezas negras son enemigas
        friends_list = white_locations  # Las piezas blancas son aliadas
    else:  # Si el caballo es negro
        friends_list = black_locations  # Las piezas negras son aliadas
        enemies_list = white_locations  # Las piezas blancas son enemigas

    # Definir las 8 posiciones posibles a las que un caballo puede moverse
    # El caballo se mueve en forma de "L": dos casillas en una dirección y una en la otra
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    # Comprobar cada movimiento posible del caballo
    for i in range(8):  # Iterar sobre las 8 posiciones posibles
        target = (position[0] + targets[i][0], position[1] + targets[i][1])  # Calcular la posición objetivo

        # Comprobar que la posición objetivo no tenga piezas aliadas y esté dentro del tablero
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)  # Si la posición es válida, se agrega a la lista de movimientos posibles

    return moves_list  # Devolver la lista de movimientos válidos para el caballo
