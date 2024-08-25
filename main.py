# ===== Ajedrez para dos jugadores importando el modulo Pygame.... Aca se configura las variables, imágenes y el bucle de juego, y movimiento de piezass =====
#=== Configuro la Ventana de la App =====
import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('¡Ajedrez para dos Jugadores!') #Titulo de la Ventana
font = pygame.font.Font('freesansbold.ttf', 20) #Fuentes de textos, esta es de uso libre
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock() #Tiempo de Actualizacion del juego
fps = 30 #Numero de fotogramas

# ===== variables e imágenes del juego =====
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #'torre', 'caballero', 'alfil', 'rey', 'reina', 'alfil', 'caballero', 'torre'.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']          #'peones'
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #'torre', 'caballero', 'alfil', 'rey', 'reina', 'alfil', 'caballero', 'torre'.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']          #'peones'
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

# ===== Estado =====
# 0 - los blancos juegan sin selección de pieza
# 1 - los blancos juegan con una pieza seleccionada
# 2 - los negros juegan sin selección de pieza
# 3 - los negros juegan con una pieza seleccionada
turn_step = 0  # Variable que indica el estado actual del turno del juego
selection = 100  # Variable que almacena el índice de la pieza seleccionada; 100 indica que no hay selección
valid_moves = []  # Lista que almacena los movimientos válidos posibles para la pieza seleccionada

# ===== Cargar en el juego imágenes de piezas (reina, rey, torre, alfil, caballo, peón) x 2 =====

black_queen = pygame.image.load('assets/images/black queen.png')  # Carga la imagen de la reina negra
black_queen = pygame.transform.scale(black_queen, (80, 80))  # Escala la reina negra a 80x80 píxeles
black_queen_small = pygame.transform.scale(black_queen, (45, 45))  # Escala la reina negra a 45x45 píxeles

black_king = pygame.image.load('assets/images/black king.png')  # Carga la imagen del rey negro
black_king = pygame.transform.scale(black_king, (80, 80))  # Escala el rey negro a 80x80 píxeles
black_king_small = pygame.transform.scale(black_king, (45, 45))  # Escala el rey negro a 45x45 píxeles

black_rook = pygame.image.load('assets/images/black rook.png')  # Carga la imagen de la torre negra
black_rook = pygame.transform.scale(black_rook, (80, 80))  # Escala la torre negra a 80x80 píxeles
black_rook_small = pygame.transform.scale(black_rook, (45, 45))  # Escala la torre negra a 45x45 píxeles

black_bishop = pygame.image.load('assets/images/black bishop.png')  # Carga la imagen del alfil negro
black_bishop = pygame.transform.scale(black_bishop, (80, 80))  # Escala el alfil negro a 80x80 píxeles
black_bishop_small = pygame.transform.scale(black_bishop, (45, 45))  # Escala el alfil negro a 45x45 píxeles

black_knight = pygame.image.load('assets/images/black knight.png')  # Carga la imagen del caballo negro
black_knight = pygame.transform.scale(black_knight, (80, 80))  # Escala el caballo negro a 80x80 píxeles
black_knight_small = pygame.transform.scale(black_knight, (45, 45))  # Escala el caballo negro a 45x45 píxeles

black_pawn = pygame.image.load('assets/images/black pawn.png')  # Carga la imagen del peón negro
black_pawn = pygame.transform.scale(black_pawn, (65, 65))  # Escala el peón negro a 65x65 píxeles
black_pawn_small = pygame.transform.scale(black_pawn, (45, 45))  # Escala el peón negro a 45x45 píxeles

white_queen = pygame.image.load('assets/images/white queen.png')  # Carga la imagen de la reina blanca
white_queen = pygame.transform.scale(white_queen, (80, 80))  # Escala la reina blanca a 80x80 píxeles
white_queen_small = pygame.transform.scale(white_queen, (45, 45))  # Escala la reina blanca a 45x45 píxeles

white_king = pygame.image.load('assets/images/white king.png')  # Carga la imagen del rey blanco
white_king = pygame.transform.scale(white_king, (80, 80))  # Escala el rey blanco a 80x80 píxeles
white_king_small = pygame.transform.scale(white_king, (45, 45))  # Escala el rey blanco a 45x45 píxeles

white_rook = pygame.image.load('assets/images/white rook.png')  # Carga la imagen de la torre blanca
white_rook = pygame.transform.scale(white_rook, (80, 80))  # Escala la torre blanca a 80x80 píxeles
white_rook_small = pygame.transform.scale(white_rook, (45, 45))  # Escala la torre blanca a 45x45 píxeles

white_bishop = pygame.image.load('assets/images/white bishop.png')  # Carga la imagen del alfil blanco
white_bishop = pygame.transform.scale(white_bishop, (80, 80))  # Escala el alfil blanco a 80x80 píxeles
white_bishop_small = pygame.transform.scale(white_bishop, (45, 45))  # Escala el alfil blanco a 45x45 píxeles

white_knight = pygame.image.load('assets/images/white knight.png')  # Carga la imagen del caballo blanco
white_knight = pygame.transform.scale(white_knight, (80, 80))  # Escala el caballo blanco a 80x80 píxeles
white_knight_small = pygame.transform.scale(white_knight, (45, 45))  # Escala el caballo blanco a 45x45 píxeles

white_pawn = pygame.image.load('assets/images/white pawn.png')  # Carga la imagen del peón blanco
white_pawn = pygame.transform.scale(white_pawn, (65, 65))  # Escala el peón blanco a 65x65 píxeles
white_pawn_small = pygame.transform.scale(white_pawn, (45, 45))  # Escala el peón blanco a 45x45 píxeles

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]  # Lista de imágenes de piezas blancas de tamaño completo
small_white_images = [white_pawn_small, white_queen_small, white_king_small, white_knight_small, white_rook_small, white_bishop_small]  # Lista de imágenes de piezas blancas a tamaño reducido

black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]  # Lista de imágenes de piezas negras de tamaño completo
small_black_images = [black_pawn_small, black_queen_small, black_king_small, black_knight_small, black_rook_small, black_bishop_small]  # Lista de imágenes de piezas negras a tamaño reducido

piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']  # Lista de nombres de piezas de ajedrez


# ===== comprobar variables/contador intermitente =====
counter = 0
winner = ''
game_over = False


# ===== Dibujo del Tablero =====
def draw_board(): #Defino la función draw_board para dibujar el tablero principal del juego.
    
    for i in range(32):# Bucle para crear los cuadrados marrones del tablero.
        column = i % 4 # Calculo la columna actual en la que se encuentra el cuadrado.
        row = i // 4 # Calculo la fila actual en la que se encuentra el cuadrado.
        if row % 2 == 0: # Si la fila es par.
            pygame.draw.rect(screen, (139, 69, 19), [600 - (column * 200), row * 100, 100, 100]) # Dibuja un rectángulo marrón (cuadrado del tablero) en la pantalla.
        else:
            pygame.draw.rect(screen, (139, 69, 19), [700 - (column * 200), row * 100, 100, 100]) # Dibuja un rectángulo marrón (cuadrado del tablero) en la pantalla para filas impares.
    pygame.draw.rect(screen, 'white', [0, 800, WIDTH, 100]) # Dibuja un rectángulo blanco en la parte inferior (mostrar mensajes o estado). 
    pygame.draw.rect(screen, 'red', [0, 800, WIDTH, 100], 5) # Dibuja un borde rojo alrededor del panel inferior
    pygame.draw.rect(screen, 'red', [800, 0, 200, HEIGHT], 5) # Dibuja un borde rojo a la derecha.
    status_text = ['Turno de la pieza Blanca', 'Selecciona el movimiento', # estado del turno.
                   'Turno de la pieza Negra', 'Selecciona el movimiento']
    screen.blit(big_font.render(status_text[turn_step], True, 'black'), (20, 820)) #Texto de estado en la parte inferior.
    for i in range(9): # Bucle para dibujar las líneas negras del tablero, tanto horizontales como verticales.
        pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2) # Dibuja una línea horizontal negra para cada fila.
        pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2) # Dibuja una línea vertical negra para cada columna.
    screen.blit(medium_font.render('Perdidas', True, 'black'), (810, 830)) # Muestra el texto "Perdidas" en la parte derecha de la pantalla, indicando un área de contadores o estadísticas.


# ===== Dibuja las piezas en el tablero =====
def draw_pieces():
    for i in range(len(white_pieces)):  # Recorre la lista de piezas blancas
        index = piece_list.index(white_pieces[i])  # Obtiene el índice de la pieza actual en la lista piece_list
        if white_pieces[i] == 'pawn':  # Verifica si la pieza actual es un peón
            screen.blit(white_pawn, (white_locations[i][0] * 100 + 22, white_locations[i][1] * 100 + 30))  # Dibuja el peón blanco en su ubicación escalada
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 100 + 10, white_locations[i][1] * 100 + 10))  # Dibuja las otras piezas blancas en sus ubicaciones escaladas
        if turn_step < 2:  # Verifica si es el turno de los blancos
            if selection == i:  # Verifica si la pieza actual está seleccionada
                pygame.draw.rect(screen, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)  # Dibuja un borde rojo alrededor de la pieza seleccionada

    for i in range(len(black_pieces)):  # Recorre la lista de piezas negras
        index = piece_list.index(black_pieces[i])  # Obtiene el índice de la pieza actual en la lista piece_list
        if black_pieces[i] == 'pawn':  # Verifica si la pieza actual es un peón
            screen.blit(black_pawn, (black_locations[i][0] * 100 + 22, black_locations[i][1] * 100 + 30))  # Dibuja el peón negro en su ubicación escalada
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 100 + 10, black_locations[i][1] * 100 + 10))  # Dibuja las otras piezas negras en sus ubicaciones escaladas
        if turn_step >= 2:  # Verifica si es el turno de los negros
            if selection == i:  # Verifica si la pieza actual está seleccionada
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)  # Dibuja un borde azul alrededor de la pieza seleccionada



# ===== Función para comprobar todas las opciones válidas de las piezas en el tablero. =====
def check_options(pieces, locations, turn):
    moves_list = []  # Inicializa una lista vacía para almacenar los movimientos válidos de la pieza actual.
    all_moves_list = []  # Inicializa una lista vacía para almacenar todos los movimientos válidos para todas las piezas.
    for i in range(len(pieces)):  # Itera a través de todas las piezas en el tablero.
        location = locations[i]  # Obtiene la ubicación actual de la pieza.
        piece = pieces[i]  # Obtiene el tipo de la pieza actual.
        if piece == 'pawn':  # Comprueba si la pieza es un peón.
            moves_list = check_pawn(location, turn)  # Llama a la función que verifica los movimientos válidos para un peón.
        elif piece == 'rook':  # Comprueba si la pieza es una torre.
            moves_list = check_rook(location, turn)  # Llama a la función que verifica los movimientos válidos para una torre.
        elif piece == 'knight':  # Comprueba si la pieza es un caballo.
            moves_list = check_knight(location, turn)  # Llama a la función que verifica los movimientos válidos para un caballo.
        elif piece == 'bishop':  # Comprueba si la pieza es un alfil.
            moves_list = check_bishop(location, turn)  # Llama a la función que verifica los movimientos válidos para un alfil.
        elif piece == 'queen':  # Comprueba si la pieza es una reina.
            moves_list = check_queen(location, turn)  # Llama a la función que verifica los movimientos válidos para una reina.
        elif piece == 'king':  # Comprueba si la pieza es un rey.
            moves_list = check_king(location, turn)  # Llama a la función que verifica los movimientos válidos para un rey.
        all_moves_list.append(moves_list)  # Agrega la lista de movimientos válidos de la pieza actual a la lista de todos los movimientos.
    return all_moves_list  # Devuelve la lista con todos los movimientos válidos de todas las piezas.



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



# ===== comprobar movimientos válidos de la reina =====
def check_queen(position, color):
    moves_list = check_bishop(position, color)  # Llama a la función check_bishop para obtener los movimientos válidos de un alfil desde la posición dada y los almacena en moves_list.
    second_list = check_rook(position, color)  # Llama a la función check_rook para obtener los movimientos válidos de una torre desde la posición dada y los almacena en second_list.
    for i in range(len(second_list)):  # Itera a través de todos los movimientos válidos obtenidos de la función check_rook. (Iteración significa repetir varias veces)
        moves_list.append(second_list[i])  # Añade cada movimiento válido de la torre a la lista de movimientos válidos de la reina (moves_list).
    return moves_list  # Devuelve la lista completa de movimientos válidos para la reina, combinando los movimientos de la torre y el alfil.



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



# ===== comprobar los movimientos de la torre =====
def check_rook(position, color):
    moves_list = []  # Lista para almacenar los movimientos posibles de la torre
    if color == 'white':  # Si la torre es blanca
        enemies_list = black_locations  # Lista de posiciones de las piezas enemigas (negras)
        friends_list = white_locations  # Lista de posiciones de las piezas aliadas (blancas)
    else:  # Si la torre es negra
        friends_list = black_locations  # Lista de posiciones de las piezas aliadas (negras)
        enemies_list = white_locations  # Lista de posiciones de las piezas enemigas (blancas)

    for i in range(4): # El bucle recorre las 4 direcciones posibles: abajo, arriba, derecha e izquierda
        path = True  # Variable para controlar si se puede seguir moviendo en la dirección actual
        chain = 1  # Contador para incrementar la distancia del movimiento en la dirección actual

        if i == 0: # Asignar valores de x e y para definir la dirección en función del valor de i
            x = 0  # No se mueve en el eje x
            y = 1  # Movimiento hacia abajo en el eje y
        elif i == 1:
            x = 0  # No se mueve en el eje x
            y = -1  # Movimiento hacia arriba en el eje y
        elif i == 2:
            x = 1  # Movimiento hacia la derecha en el eje x
            y = 0  # No se mueve en el eje y
        else:
            x = -1  # Movimiento hacia la izquierda en el eje x
            y = 0  # No se mueve en el eje y

        
        while path: # Mientras el camino sea válido (es decir, no hay obstrucciones ni fuera del tablero)     
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7: # Comprobar si la posición nueva no está ocupada por una pieza aliada y si está dentro del tablero    
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y))) # Añadir la nueva posición como un movimiento válido
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list: # Si la posición tiene una pieza enemiga, se detiene el camino en esa dirección
                    path = False      
                chain += 1 # Incrementar la cadena para continuar verificando la siguiente posición en esa dirección
            else:     
                path = False # Si la nueva posición no es válida (obstáculo o fuera del tablero), se detiene el camino
    return moves_list  # Devolver la lista de movimientos válidos para la torre


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



# ===== comprobar movimientos válidos para la pieza seleccionada =====
def check_valid_moves():  # Función para comprobar los movimientos válidos de la pieza seleccionada
    if turn_step < 2:  # Si el turno está en la fase inicial (turnos de las blancas)
        options_list = white_options  # Usar las opciones de movimiento para las piezas blancas
    else:  # Si no está en la fase inicial (turnos de las negras)
        options_list = black_options  # Usar las opciones de movimiento para las piezas negras
    
    valid_options = options_list[selection]  # Obtener las opciones válidas para la pieza actualmente seleccionada
    
    return valid_options  # Devolver los movimientos válidos para la pieza seleccionada



# ===== Dibujar movimientos válidos en la pantalla =====
def draw_valid(moves):  # Función para dibujar los movimientos válidos en la pantalla
    if turn_step < 2:  # Si es el turno de las blancas
        color = 'red'  # Usar el color rojo para indicar los movimientos válidos
    else:  # Si es el turno de las negras
        color = 'blue'  # Usar el color azul para indicar los movimientos válidos
    
    for i in range(len(moves)):  # Recorrer cada movimiento válido
        pygame.draw.circle(screen, color, (moves[i][0] * 100 + 50, moves[i][1] * 100 + 50), 5)  # Dibujar un círculo pequeño en la posición del movimiento válido
        # La posición del círculo se calcula multiplicando las coordenadas del movimiento por 100 (tamaño de casilla) y sumando 50 para centrarlo



# ===== Dibuja las piezas capturadas en el costado de la pantalla. Lado derecho =====
def draw_captured():  # Función para dibujar las piezas capturadas en el costado derecho de la pantalla
    for i in range(len(captured_pieces_white)):  # Recorre la lista de piezas capturadas por las blancas
        captured_piece = captured_pieces_white[i]  # Obtiene la pieza capturada actual
        index = piece_list.index(captured_piece)  # Obtiene el índice de la pieza en la lista de piezas para encontrar su imagen correspondiente
        screen.blit(small_black_images[index], (825, 5 + 50 * i))  # Dibuja la imagen de la pieza en la posición correspondiente en el lado derecho (columna 825)
    
    for i in range(len(captured_pieces_black)):  # Recorre la lista de piezas capturadas por las negras
        captured_piece = captured_pieces_black[i]  # Obtiene la pieza capturada actual
        index = piece_list.index(captured_piece)  # Obtiene el índice de la pieza en la lista de piezas para encontrar su imagen correspondiente
        screen.blit(small_white_images[index], (925, 5 + 50 * i))  # Dibuja la imagen de la pieza en la posición correspondiente en el lado derecho (columna 925)


#Salir de la ventana
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    
pygame.display.flip()
pygame.quit()