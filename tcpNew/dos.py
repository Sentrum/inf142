from os import environ
from socket import create_connection

server = environ.get("SERVER", "localhost")
sockets = [create_connection(("localhost", 5550)) for _ in range(2000)]
