FROM ubuntu:latest

RUN apt update && apt upgrade -y && apt install python3 -y && apt install python3-pip -y && apt install redis -y && apt install git -y && apt install autoremove -y

RUN git clone git@github.com:um-computacion-tm/ajedrez-2024-GALBARRACIN.git

WORKDIR /ajedrez-2024-GALBARRACIN

RUN pip3 install -r requirements.txt

CMD python3 chess_game_console/main.py
