#Ajedredez con modulo PyGame

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

# bucle principal del juego
run = True
while run:
    timer.tick(fps)
    screen.fill('light yellow') #Color de Fondo

# variables e imágenes del juego

white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #'torre', 'caballero', 'alfil', 'rey', 'reina', 'alfil', 'caballero', 'torre'.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']          #'peones'
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook', #'torre', 'caballero', 'alfil', 'rey', 'reina', 'alfil', 'caballero', 'torre'.
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']          #'peones'
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = [] #piezas capuradas blancas
captured_pieces_black = [] #piezas capturadas negras

# Estado 
# 0 - los blancos giran sin selección: 1 - los blancos giran pieza seleccionada: 2 - los negros giran sin selección, 3 - los negros giran pieza seleccionada
turn_step = 0
selection = 100
valid_moves = []

# Dibujo del Tablero 
def draw_board(): #Definir la función draw_board para dibujar el tablero principal del juego.
    
    for i in range(32):# Bucle para crear los cuadrados marrones del tablero.
        column = i % 4 # Calcula la columna actual en la que se encuentra el cuadrado.
        row = i // 4 # Calcula la fila actual en la que se encuentra el cuadrado.
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