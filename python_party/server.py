import socket

host = 'localhost'
port = 8080
server_address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(2)

conn, adress = server_socket.accept()
print("Connection from: " + str(adress))

data = conn.recv(1024).decode()

print("From connected user: " + str(data))

conn.close()