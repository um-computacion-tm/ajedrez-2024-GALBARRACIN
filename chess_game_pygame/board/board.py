import pygame

from pieces.bishop import check_bishop
from pieces.king import check_king
from pieces.knight import check_knight
from pieces.pawn import check_pawn
from pieces.queen import check_queen
from pieces.rook import check_rook

# ===== variables e imágenes del juego =====
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',  # Lista de piezas blancas: torre, caballero, alfil, rey, reina, alfil, caballero, torre.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']           # Lista de peones blancos.
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),        # Posiciones iniciales de las piezas blancas en el tablero.
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]        # Posiciones iniciales de los peones blancos.

black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',  # Lista de piezas negras: torre, caballero, alfil, rey, reina, alfil, caballero, torre.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']           # Lista de peones negros.
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),        # Posiciones iniciales de las piezas negras en el tablero.
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]        # Posiciones iniciales de los peones negros.

captured_pieces_white = []  # Lista vacía para almacenar las piezas negras capturadas por el jugador blanco.
captured_pieces_black = []  # Lista vacía para almacenar las piezas blancas capturadas por el jugador negro.



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



# ===== dibuja un cuadrado parpadeante alrededor del rey si está en jaque =====
def draw_check():  # Función para dibujar un cuadro parpadeante alrededor del rey si está en jaque
    if turn_step < 2:  # Verifica si es el turno de las blancas
        if 'king' in white_pieces:  # Comprueba si el rey blanco sigue en el tablero
            king_index = white_pieces.index('king')  # Obtiene el índice del rey blanco
            king_location = white_locations[king_index]  # Obtiene la posición del rey blanco
            for i in range(len(black_options)):  # Recorre todas las opciones de movimiento de las piezas negras
                if king_location in black_options[i]:  # Verifica si alguna pieza negra amenaza al rey blanco
                    if counter < 15:  # Controla el parpadeo; si el contador es menor a 15, dibuja el cuadro
                        pygame.draw.rect(screen, 'dark red', [white_locations[king_index][0] * 100 + 1,  # Dibuja un rectángulo alrededor del rey blanco
                                                              white_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:  # Verifica si es el turno de las negras
        if 'king' in black_pieces:  # Comprueba si el rey negro sigue en el tablero
            king_index = black_pieces.index('king')  # Obtiene el índice del rey negro
            king_location = black_locations[king_index]  # Obtiene la posición del rey negro
            for i in range(len(white_options)):  # Recorre todas las opciones de movimiento de las piezas blancas
                if king_location in white_options[i]:  # Verifica si alguna pieza blanca amenaza al rey negro
                    if counter < 15:  # Controla el parpadeo; si el contador es menor a 15, dibuja el cuadro
                        pygame.draw.rect(screen, 'dark blue', [black_locations[king_index][0] * 100 + 1,  # Dibuja un rectángulo alrededor del rey negro
                                                               black_locations[king_index][1] * 100 + 1, 100, 100], 5)

# ===== dibuja el mensaje de "game over" y opción de reinicio =====
def draw_game_over():  # Función para dibujar la pantalla de "game over"
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])  # Dibuja un rectángulo negro en el centro de la pantalla
    screen.blit(font.render(f'{winner} Ganaste el Juego', True, 'white'), (210, 210))  # Muestra el mensaje de ganador
    screen.blit(font.render(f'Presiona ENTER para Reiniciar', True, 'white'), (210, 240))  # Muestra la opción para reiniciar el juego

