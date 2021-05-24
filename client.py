from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)

while(text := input("> ").lower()) != "shut down":
    sock.sendto(text.encode(), ("81.191.115.9", 55551))
