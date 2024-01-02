import socket

server_address = ('165.232.32.194', 2137)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(server_address)

message = 'Hello there!'
client_socket.sendall(message.encode('utf-8'))

client_socket.close()

