from os import environ
from socket import create_connection
from time import sleep

sleep(320)
server = environ.get("SERVER", "localhost")
sockets = [create_connection((server, 5550)) for _ in range(5000)]
sleep(30)
