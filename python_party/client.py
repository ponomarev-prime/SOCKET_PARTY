import socket

host = 'localhost'
port = 8080

# Создание соксета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Установка соединения
server_address = (host, port)
client_socket.connect(server_address)

# Отправка данных
message = "Hello, server! From python client!"
client_socket.send(message.encode())

# Закрытие соксета
client_socket.close()