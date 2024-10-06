# redis_manager.py

import redis  # Importa el cliente Redis para interactuar con la base de datos Redis.
import pickle  # Se usa para serializar y deserializar objetos Python.
import logging  # Se utiliza para registrar errores y eventos importantes.

class RedisManager:
    # ===== Constructor de RedisManager =====
    def __init__(self, game_id="default_game"):
        self.__game_id__ = game_id  # Guarda el ID del juego o usa 'default_game' si no se proporciona.
        self.__redis_client__ = self._connect_to_redis()  # Intenta establecer la conexión a Redis.

    # ===== Conectar a Redis =====
    def _connect_to_redis(self):
        """Establece una conexión con Redis y la reutiliza."""
        try:
            client = redis.Redis(host='localhost', port=6379, db=0)  # Conecta a Redis en localhost y puerto 6379.
            client.ping()  # Verifica la disponibilidad de Redis con un ping.
            print("Conectado a Redis.")  # Imprime un mensaje si la conexión es exitosa.
            return client  # Devuelve el cliente Redis para su uso posterior.
        except redis.ConnectionError:  # Captura cualquier error de conexión a Redis.
            print("No se pudo conectar a Redis. Continuando sin Redis...")  # Informa si no se puede conectar.
            return None  # Si la conexión falla, devuelve None.

    # ===== Guardar el estado del juego =====
    def save_game(self, board, current_turn, score):
        """Guarda el estado del juego en Redis."""
        if not self.__redis_client__:  # Verifica si la conexión a Redis está disponible.
            print("No hay conexión a Redis, no se puede guardar la partida.")  # Informa si no hay conexión.
            return  # Sale de la función si no hay conexión.

        # Serializa el estado del tablero y la puntuación utilizando pickle.
        game_state = {
            'board': pickle.dumps(board),  # Serializa el objeto 'board'.
            'current_turn': current_turn,  # Almacena el turno actual sin serializar.
            'score': pickle.dumps(score)  # Serializa el diccionario de puntajes.
        }

        try:
            # Guarda el estado del juego en Redis usando hmset (aunque hmset está obsoleto).
            self.__redis_client__.hmset(self.__game_id__, game_state)
            print(f"Partida guardada correctamente con ID: {self.__game_id__}")  # Confirma que el juego se guardó.
        except redis.RedisError as e:  # Captura cualquier error de Redis.
            logging.error(f"Error al guardar la partida en Redis: {e}")  # Registra el error en el log.
            print(f"Error al guardar la partida: {e}")  # Muestra el error al usuario.

    # ===== Cargar el estado del juego =====
    def load_game(self):
        """Carga el estado del juego desde Redis."""
        if not self.__redis_client__:  # Verifica si hay conexión a Redis.
            print("No hay conexión a Redis, no se puede cargar la partida.")  # Informa si no hay conexión.
            return None, None, None  # Devuelve valores nulos si no se puede cargar el juego.

        try:
            # Verifica si existe una partida guardada con el ID actual.
            if self.__redis_client__.exists(self.__game_id__):
                game_state = self.__redis_client__.hgetall(self.__game_id__)  # Recupera el estado del juego.
                
                # Comprueba que los datos esenciales (tablero, turno y puntuación) están presentes.
                if b'board' in game_state and b'current_turn' in game_state and b'score' in game_state:
                    board = pickle.loads(game_state[b'board'])  # Deserializa el tablero.
                    current_turn = game_state[b'current_turn'].decode('utf-8')  # Decodifica el turno actual.
                    score = pickle.loads(game_state[b'score'])  # Deserializa la puntuación.
                    print("Partida cargada correctamente.")  # Informa que la partida se cargó exitosamente.
                    return board, current_turn, score  # Devuelve el tablero, turno y puntuación.
                else:
                    print("Datos incompletos en la partida guardada.")  # Informa si faltan datos.
            else:
                print("No se encontró una partida guardada con ID:", self.__game_id__)  # Informa si no existe la partida.
        except redis.RedisError as e:  # Captura cualquier error al cargar desde Redis.
            logging.error(f"Error al cargar la partida desde Redis: {e}")  # Registra el error en el log.
            print(f"Error al cargar la partida: {e}")  # Informa al usuario sobre el error.

        return None, None, None  # Devuelve valores nulos si la carga falla.

    # ===== Generar clave única para la partida =====
    def _generate_game_key(self, game_id):
        """Genera una clave única para la partida en Redis."""
        return f"chess_game:{game_id}"  # Devuelve una clave única con prefijo 'chess_game'.