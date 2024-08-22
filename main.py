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