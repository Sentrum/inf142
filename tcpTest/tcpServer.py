from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)

sock.bind(("localhost", 4444))
#listen for connection
sock.listen()
print("The server is ready to recieve")
while True:
    conn, _ = sock.accept()
    sentence = conn.recv(1024).decode()
    new_sentence = sentence.upper()
    conn.send(new_sentence.encode())
    conn.close()