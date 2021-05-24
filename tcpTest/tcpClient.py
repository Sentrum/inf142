from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)

ip = "localhost"
portnum = 4444
server_address = (ip, portnum)

sock.connect(server_address)

sentence = input("Input lowercase sentence: ")
sock.send(sentence.encode())
new_sentence = sock.recv(1024).decode()
print(f"From server: {new_sentence}")
sock.close()