from socket import socket, AF_INET, SOCK_DGRAM
#Dgram to say its a udp

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(("81.191.115.9", 55551))

while True:
    msg, addr = sock.recvfrom(2048)
    print(f"{addr[0]}  says {msg.decode()}") 

