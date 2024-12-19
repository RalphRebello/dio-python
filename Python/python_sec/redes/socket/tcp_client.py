import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Conexão falhou')
        print(e)
        sys.exit()

    print('Socket criado com sucesso')

    host_alvo = input(f'Host ou ip para conectar -> ')
    port_alvo = input(f'Porta para conectar -> ')

    try:
        s.connect((host_alvo, int(port_alvo)))
        print(f'Cliente TCP conectado ao host {host_alvo} na porta {port_alvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Conexão falhou no {host_alvo} e porta {port_alvo}')
        print(e)
        sys.exit()


if __name__ == '__main__':
    main()