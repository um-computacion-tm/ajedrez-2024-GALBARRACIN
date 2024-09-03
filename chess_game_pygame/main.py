# ===== Ajedrez para dos jugadores importando el modulo Pygame.... Aca se configura las variables, imágenes y el bucle de juego, y movimiento de piezass =====

# ===== Configuro la Ventana de la App =====
import pygame  # Importa la biblioteca Pygame, que se utiliza para desarrollar juegos y aplicaciones multimedia.


pygame.init()  # Inicializa todos los módulos de Pygame.

WIDTH = 1000  # Define el ancho de la ventana del juego en píxeles.
HEIGHT = 900  # Define la altura de la ventana del juego en píxeles.
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Crea la ventana del juego con el tamaño especificado.
pygame.display.set_caption('¡Ajedrez para dos Jugadores!')  # Establece el título de la ventana.

font = pygame.font.Font('freesansbold.ttf', 20)  # Carga una fuente de texto con un tamaño de 20 píxeles.
medium_font = pygame.font.Font('freesansbold.ttf', 40)  # Carga la misma fuente pero con un tamaño de 40 píxeles.
big_font = pygame.font.Font('freesansbold.ttf', 50)  # Carga la misma fuente pero con un tamaño de 50 píxeles.

timer = pygame.time.Clock()  # Crea un objeto de reloj para controlar la tasa de fotogramas del juego.
fps = 30  # Establece la cantidad de fotogramas por segundo (FPS) para la ejecución del juego.



# ===== Estado =====
# 0 - los blancos juegan sin selección de pieza
# 1 - los blancos juegan con una pieza seleccionada
# 2 - los negros juegan sin selección de pieza
# 3 - los negros juegan con una pieza seleccionada
turn_step = 0  # Variable que indica el estado actual del turno del juego
selection = 100  # Variable que almacena el índice de la pieza seleccionada; 100 indica que no hay selección
valid_moves = []  # Lista que almacena los movimientos válidos posibles para la pieza seleccionada




# ===== comprobar variables/contador intermitente =====
counter = 0  # Inicializa un contador a 0, que se usa para controlar eventos temporales, como el parpadeo de la casilla en jaque.
winner = ''  # Inicializa la variable para almacenar el ganador del juego, comenzando como una cadena vacía.
game_over = False  # Inicializa el estado del juego como no terminado, para determinar si el juego está en curso o ha finalizado.



# ===== bucle principal del juego =====
black_options = check_options(black_pieces, black_locations, 'black')  # Calcula las opciones de movimiento para las piezas negras
white_options = check_options(white_pieces, white_locations, 'white')  # Calcula las opciones de movimiento para las piezas blancas
run = True  # Variable para controlar el bucle principal del juego
while run:  # Bucle principal que mantiene el juego en marcha
    timer.tick(fps)  # Controla la velocidad del juego en función de los frames por segundo (fps)
    if counter < 30:  # Controla un contador para efectos como el parpadeo
        counter += 1  # Incrementa el contador
    else:
        counter = 0  # Reinicia el contador si alcanza 30
    screen.fill('light yellow')  # Rellena la pantalla con un color de fondo amarillo claro
    draw_board()  # Dibuja el tablero en la pantalla
    draw_pieces()  # Dibuja las piezas en sus posiciones actuales
    draw_captured()  # Dibuja las piezas capturadas en un lado de la pantalla
    draw_check()  # Dibuja un cuadro parpadeante alrededor del rey si está en jaque
    if selection != 100:  # Verifica si hay una pieza seleccionada (100 indica que no hay ninguna seleccionada)
        valid_moves = check_valid_moves()  # Obtiene los movimientos válidos para la pieza seleccionada
        draw_valid(valid_moves)  # Dibuja los movimientos válidos para la pieza seleccionada en la pantalla


# ===== manejo de eventos =====
    for event in pygame.event.get():  # Itera sobre todos los eventos que ocurren durante el juego
        if event.type == pygame.QUIT:  # Si el evento es de tipo QUIT (cerrar la ventana)
            run = False  # Termina el bucle principal del juego

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not game_over:  # Si se presiona el botón izquierdo del mouse y el juego no ha terminado
            x_coord = event.pos[0] // 100  # Calcula la coordenada x en términos de casillas de 100 píxeles
            y_coord = event.pos[1] // 100  # Calcula la coordenada y en términos de casillas de 100 píxeles
            click_coords = (x_coord, y_coord)  # Guarda las coordenadas del clic en una tupla

            if turn_step <= 1:  # Si es el turno del jugador con piezas blancas
                if click_coords == (8, 8) or click_coords == (9, 8):  # Si se hace clic en una casilla específica para rendirse
                    winner = 'black'  # El jugador negro gana

                if click_coords in white_locations:  # Si se hace clic en una casilla con una pieza blanca
                    selection = white_locations.index(click_coords)  # Selecciona la pieza blanca que se ha clicado
                    if turn_step == 0:  # Si es el primer paso del turno
                        turn_step = 1  # Avanza al segundo paso del turno

                if click_coords in valid_moves and selection != 100:  # Si se hace clic en una casilla válida para moverse y hay una pieza seleccionada
                    white_locations[selection] = click_coords  # Mueve la pieza seleccionada a la nueva ubicación

                    if click_coords in black_locations:  # Si la nueva ubicación tiene una pieza enemiga
                        black_piece = black_locations.index(click_coords)  # Identifica la pieza negra en la casilla
                        captured_pieces_white.append(black_pieces[black_piece])  # Añade la pieza capturada a la lista de piezas capturadas por las blancas
                        if black_pieces[black_piece] == 'king':  # Si la pieza capturada es el rey
                            winner = 'BLANCO'  # El jugador blanco gana
                        black_pieces.pop(black_piece)  # Elimina la pieza negra capturada
                        black_locations.pop(black_piece)  # Elimina la ubicación de la pieza capturada

                    black_options = check_options(black_pieces, black_locations, 'black')  # Actualiza las opciones de movimiento para las piezas negras
                    white_options = check_options(white_pieces, white_locations, 'white')  # Actualiza las opciones de movimiento para las piezas blancas
                    turn_step = 2  # Cambia al turno del jugador negro
                    selection = 100  # Reinicia la selección de pieza
                    valid_moves = []  # Limpia los movimientos válidos

            if turn_step > 1:  # Si es el turno del jugador con piezas negras
                if click_coords == (8, 8) or click_coords == (9, 8):  # Si se hace clic en una casilla específica para rendirse
                    winner = 'BLANCO'  # El jugador blanco gana

                if click_coords in black_locations:  # Si se hace clic en una casilla con una pieza negra
                    selection = black_locations.index(click_coords)  # Selecciona la pieza negra que se ha clicado
                    if turn_step == 2:  # Si es el primer paso del turno del jugador negro
                        turn_step = 3  # Avanza al siguiente paso del turno

                if click_coords in valid_moves and selection != 100:  # Si se hace clic en una casilla válida para moverse y hay una pieza seleccionada
                    black_locations[selection] = click_coords  # Mueve la pieza seleccionada a la nueva ubicación

                    if click_coords in white_locations:  # Si la nueva ubicación tiene una pieza enemiga
                        white_piece = white_locations.index(click_coords)  # Identifica la pieza blanca en la casilla
                        captured_pieces_black.append(white_pieces[white_piece])  # Añade la pieza capturada a la lista de piezas capturadas por las negras
                        if white_pieces[white_piece] == 'king':  # Si la pieza capturada es el rey
                            winner = 'NEGRO'  # El jugador negro gana
                        white_pieces.pop(white_piece)  # Elimina la pieza blanca capturada
                        white_locations.pop(white_piece)  # Elimina la ubicación de la pieza capturada

                    black_options = check_options(black_pieces, black_locations, 'black')  # Actualiza las opciones de movimiento para las piezas negras
                    white_options = check_options(white_pieces, white_locations, 'white')  # Actualiza las opciones de movimiento para las piezas blancas
                    turn_step = 0  # Cambia al turno del jugador blanco
                    selection = 100  # Reinicia la selección de pieza
                    valid_moves = []  # Limpia los movimientos válidos

        if event.type == pygame.KEYDOWN and game_over:  # Si se presiona una tecla y el juego ha terminado
            if event.key == pygame.K_RETURN:  # Si se presiona la tecla ENTER
                game_over = False  # Reinicia el estado del juego
                winner = ''  # Limpia el ganador

                # Reinicia las piezas y sus ubicaciones para ambos jugadores
                white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_pieces_white = []  # Limpia las piezas capturadas por las blancas
                captured_pieces_black = []  # Limpia las piezas capturadas por las negras
                turn_step = 0  # Reinicia el paso del turno
                selection = 100  # Reinicia la selección de pieza
                valid_moves = []  # Limpia los movimientos válidos
                black_options = check_options(black_pieces, black_locations, 'black')  # Recalcula las opciones de movimiento para las piezas negras
                white_options = check_options(white_pieces, white_locations, 'white')  # Recalcula las opciones de movimiento para las piezas blancas

    if winner != '':  # Si ya hay un ganador
        game_over = True  # Establece el estado del juego como terminado
        draw_game_over()  # Muestra el mensaje de fin de juego

    pygame.display.flip()  # Actualiza la pantalla con todos los cambios realizados
pygame.quit()  # Termina la ejecución del juego

