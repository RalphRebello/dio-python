from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        print(f'{piloto}: km {trajeto}')


t_carro1 = Thread(target=carro, args=[1, 'Ralph'])
t_carro2 = Thread(target=carro, args=[1.5, 'Hina'])

t_carro1.start()
t_carro2.start()