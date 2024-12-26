import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente socket criado com sucesso')

host = 'localhost'
port = 5433
message = 'hello-old-old server'

try:
    print(f'Cliente: {message}')
    s.sendto(message.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()

    print(f'Client {dados}')
finally:
    print('Client: fechando a conexão')
    s.close()