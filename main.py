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