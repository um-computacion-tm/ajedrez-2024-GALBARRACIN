# Ajedrez para dos jugadores importando el modulo Pygame.... Aca se configura las variables, imágenes y el bucle de juego

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

# variables e imágenes del juego
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

# Estado
# 0 - los blancos juegan sin selección de pieza
# 1 - los blancos juegan con una pieza seleccionada
# 2 - los negros juegan sin selección de pieza
# 3 - los negros juegan con una pieza seleccionada
turn_step = 0  # Variable que indica el estado actual del turno del juego
selection = 100  # Variable que almacena el índice de la pieza seleccionada; 100 indica que no hay selección
valid_moves = []  # Lista que almacena los movimientos válidos posibles para la pieza seleccionada

# Cargar en el juego imágenes de piezas (reina, rey, torre, alfil, caballo, peón) x 2

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

# Dibujo del Tablero 
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
    
#Salir de la ventana
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False
    
pygame.display.flip()
pygame.quit()