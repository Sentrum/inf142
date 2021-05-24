from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR
#initiate socket
sock = socket(AF_INET, SOCK_DGRAM)

#Ip and ports this UDP connection uses
host = "localhost"
port = 5555
#tuple
socket_address = (host, port)
#Used to not collide with allready used ports and pass a socket option // reuse an address
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#binds the socket to the host and port
sock.bind(socket_address)



for size in range(5, 10):
    data, _ = sock.recvfrom(size)
    message = data.decode()
    print(f"Recieved message: {message}")