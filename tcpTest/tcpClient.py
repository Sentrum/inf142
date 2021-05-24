from socket import socket

sock = socket() #  AF_INET, SOCK_STREAM
#Connection variables
ip = "localhost"
portnum = 4444
server_address = (ip, portnum)
###CONTEXT MANAGER
sock.connect(server_address)

sentence = input("Input lowercase sentence: ")
sock.send(sentence.encode())
new_sentence = sock.recv(1024).decode()
print(f"From server: {new_sentence}")
sock.close()