# imagen base
FROM python:3-alpine

# Actualizar el sistema e instalar las dependencias necesarias
RUN apk add --no-cache git redis

# Clonar el repositorio (HTTPS si es público)
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-GALBARRACIN.git

# Cambiar el directorio de trabajo a chess_game_console
WORKDIR /ajedrez-2024-GALBARRACIN

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Instalar redis-py si no está en requirements.txt
RUN pip install redis

# Pone a la vista el puerto para que se conecte
EXPOSE 6379

# Comando por defecto para ejecutar el script principal
CMD ["sh", "-c","redis-server --daemonize yes && coverage run -m unittest discover chess_game_console && coverage report -m && python chess_game_console/main.py"]

#nano Dockerfile = Edito el contenido del Docker 
#ls Dockerfile = selecciono de la lista

#sudo docker --tag ajedrez .
#sudo docker run -i ajedrez 