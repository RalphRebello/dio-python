class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando motor')

    def __str__(self):
        return (f'{self.__class__.__name__}: '
                f'{", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}')


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{"sim" if self.carregado else "nao"} estou carregado')


moto = Motocicleta('preta', 'abc1234', 2)
carro = Carro('branco', 'xyz4321', 4)
caminhao = Caminhao('roxo', 'gfd1423', 8, False)

print(f'{moto}\n{carro}\n{caminhao}')
