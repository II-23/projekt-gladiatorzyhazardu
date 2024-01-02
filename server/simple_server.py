import socket

server_address = ('0.0.0.0', 2137)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(server_address)

server_socket.listen(1)
print('Server listening on {}:{}'.format(*server_address))

client_socket, client_address = server_socket.accept()
print('Connection from:', client_address)

while True:
    data = client_socket.recv(1024)

    if not data:
        break
    
    print('Received:', data.decode('utf-8'))

client_socket.close()
server_socket.close()

