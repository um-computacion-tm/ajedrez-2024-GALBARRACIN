from board.board import black_locations, white_locations

# ===== comprobar los movimientos del alfil =====
def check_bishop(position, color):
    moves_list = []  # Lista para almacenar los movimientos posibles del alfil
    if color == 'white':  # Si el color del alfil es blanco
        enemies_list = black_locations  # Lista de posiciones de las piezas enemigas (negras)
        friends_list = white_locations  # Lista de posiciones de las piezas aliadas (blancas)
    else:  # Si el color del alfil es negro
        friends_list = black_locations  # Lista de posiciones de las piezas aliadas (negras)
        enemies_list = white_locations  # Lista de posiciones de las piezas enemigas (blancas)
    for i in range(4): # El bucle recorre las 4 direcciones diagonales: arriba a la derecha, arriba a la izquierda, abajo a la derecha, abajo a la izquierda
        path = True  # Variable para controlar si se puede seguir moviendo en la dirección actual
        chain = 1  # Contador para incrementar la distancia del movimiento en la dirección actual
        # Asignar valores de x e y para definir la dirección en función del valor de i
        if i == 0:
            x = 1  # Movimiento hacia la derecha
            y = -1  # Movimiento hacia arriba
        elif i == 1:
            x = -1  # Movimiento hacia la izquierda
            y = -1  # Movimiento hacia arriba
        elif i == 2:
            x = 1  # Movimiento hacia la derecha
            y = 1  # Movimiento hacia abajo
        else:
            x = -1  # Movimiento hacia la izquierda
            y = 1  # Movimiento hacia abajo
        while path: # Mientras el camino sea válido (es decir, no hay obstrucciones ni fuera del tablero)
            
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7: # Comprobar si la posición nueva no está ocupada por una pieza aliada y si está dentro del tablero
                
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y))) # Añadir la nueva posición como un movimiento válido
                
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list: # Si la posición tiene una pieza enemiga, se detiene el camino en esa dirección
                    path = False
                
                chain += 1 # Incrementar la cadena para continuar verificando la siguiente posición en esa dirección
            else:
                
                path = False # Si la nueva posición no es válida (obstáculo o fuera del tablero), se detiene el camino
    return moves_list  # Devolver la lista de movimientos válidos para el alfil
