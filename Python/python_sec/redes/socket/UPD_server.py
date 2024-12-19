import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Server socket criado com sucesso')


host = 'localhost'
port = 5432

s.bind((host, port))
message = 'Server: Hello client'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Server send message')
        s.sendto(dados + (message.encode()), end)
