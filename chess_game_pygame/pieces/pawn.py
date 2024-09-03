
# ===== comprobar movimientos de peón válidos =====
def check_pawn(position, color):
    moves_list = []  # Lista para almacenar los movimientos posibles del peón

    if color == 'white':  # Si el peón es blanco
        # Comprobar si el peón puede moverse un paso hacia adelante
        if (position[0], position[1] + 1) not in white_locations and \
                (position[0], position[1] + 1) not in black_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))

        # Comprobar si el peón está en su posición inicial para avanzar dos pasos
        if (position[0], position[1] + 2) not in white_locations and \
                (position[0], position[1] + 2) not in black_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))

        # Comprobar si puede capturar una pieza enemiga diagonalmente a la derecha
        if (position[0] + 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] + 1, position[1] + 1))

        # Comprobar si puede capturar una pieza enemiga diagonalmente a la izquierda
        if (position[0] - 1, position[1] + 1) in black_locations:
            moves_list.append((position[0] - 1, position[1] + 1))

    else:  # Si el peón es negro
        # Comprobar si el peón puede moverse un paso hacia adelante
        if (position[0], position[1] - 1) not in white_locations and \
                (position[0], position[1] - 1) not in black_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))

        # Comprobar si el peón está en su posición inicial para avanzar dos pasos
        if (position[0], position[1] - 2) not in white_locations and \
                (position[0], position[1] - 2) not in black_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))

        # Comprobar si puede capturar una pieza enemiga diagonalmente a la derecha
        if (position[0] + 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] + 1, position[1] - 1))

        # Comprobar si puede capturar una pieza enemiga diagonalmente a la izquierda
        if (position[0] - 1, position[1] - 1) in white_locations:
            moves_list.append((position[0] - 1, position[1] - 1))

    return moves_list  # Devolver la lista de movimientos válidos para el peón
