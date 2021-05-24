from socket import socket, AF_INET, SOCK_DGRAM 

#initiating socket
sock = socket(AF_INET, SOCK_DGRAM)

#connects to the server
server_address = ("localhost", 5555)

data = "nice!".encode()
for _ in range(5):
    size = sock.sendto(data, ("localhost", 5555))
    print(f"Sent {size} bytes")
