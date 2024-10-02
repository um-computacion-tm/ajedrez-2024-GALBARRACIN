# Juego de Ajedrez en Python en Consola


Este es un juego de ajedrez de consola escrito en Python. Permite a dos jugadores jugar utilizando comandos de texto en la consola.


# Requisitos


Tener instalado Python 3.x
Instalar Redis (pip install)


# Cómo Ejecutar el Juego


Clona este repositorio o descarga la carpeta "chess_game_console" manualmente en tu máquina.


Ejecuta el archivo chess.py para iniciar el juego: " python chess.py"


# Interacción del Juego:


Juego por turnos, comienza el jugador blanco.
Cada jugador puede introducir comandos para mover piezas utilizando la notación de ajedrez estándar (por ejemplo, "e2 e4").
Para mover una pieza, utiliza el comando mover seguido de las posiciones de origen y destino. Ejemplo: mover e2 e4.
Para salir del juego, escribe salir.


# Reglas del Juego


El juego sigue las reglas estándar del ajedrez, las piezas se capturan moviéndose a la casilla ocupada por una pieza del oponente.
El juego alterna automáticamente entre los jugadores después de cada movimiento válido.


# Movimientos de Piezas:


Peón (P): Se mueve hacia adelante una casilla o dos desde su posición inicial; captura en diagonal.
Torre (R): Se mueve en línea recta tanto horizontal como verticalmente.
Caballo (N): Se mueve en forma de 'L': dos casillas en una dirección y una en perpendicular.
Alfil (B): Se mueve en diagonal tantas casillas como quiera.
Reina (Q): Combina los movimientos de la Torre y el Alfil.
Rey (K): Se mueve una casilla en cualquier dirección.


# Puntaje: El juego muestra el puntaje en función de las piezas capturadas:


- Peón (P): 1 punto
- Caballo (N): 3 puntos
- Alfil (B): 3 puntos
- Torre (R): 5 puntos
- Reina (Q): 9 puntos
- Rey (K): 0 Fin del juego
# Personalización


Puedes personalizar el juego modificando el código en los diferentes archivos de piezas en el directorio pieces/. Cada pieza tiene su propia clase con su lógica de movimiento en su archivo correspondiente.


# Seleccionar posición


mover <posición_inicial> <posición_destino>


# Coordenadas


- 8 r n b q k b n r
- 7 p p p p p p p p
- 6 - - - - - - - -
- 5 - - - - - - - -
- 4 - - - - - - - -
- 3 - - - - - - - -
- 2 P P P P P P P P
- 1 R N B Q K B N R
-   a b c d e f g h


# Salir del juego


Escribir " salir " en la consola




# Cómo Ejecutar las Pruebas


Para ejecutar las pruebas unitarias, navega a la carpeta principal en la terminal y ejecuta el siguiente comando:


" python -m unittest discover -s tests "


# Ejemplo Test de manera individual


" python -m unittest tests.test_bishop "


## Funcionamiento Redis


En el constructor de la clase Chess, se añadió la conexión a un servidor Redis. Se utiliza el cliente Redis de Python (redis-py) y se conecta a un servidor en localhost por defecto.


# Guardado del estado del juego


El método save_game() serializa el estado actual del tablero, el turno del jugador, y la puntuación usando pickle, almacena estos datos en Redis. El estado se guarda con una clave única basada en el game_id.


# Carga del estado del juego


El método load_game() carga los datos guardados desde Redis, deserializa el tablero y restaura el turno y las puntuaciones.


# Manejo de identificadores de partidas


El juego permite a los jugadores ingresar un game_id para continuar una partida previamente guardada. Si no se introduce un game_id, se empieza una nueva partida.


# Comando para guardar la partida


Se ha añadido el comando guardar, que permite al jugador guardar el estado actual del juego en Redis y retomarlo más tarde.
