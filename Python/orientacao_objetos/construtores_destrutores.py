class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe")
        self.nome = nome
        self.cor = cor
        self.arcordado = acordado

    def __del__(self):
        print('Removendo a instancia da classe')

    def falar(self):
        print('auau')


def criar_cachorro():
    c = Cachorro('Zeus', 'Branco e preto', False)
    print(c.nome)

criar_cachorro()
c = Cachorro('Chappie', 'amarelo')
c.falar()

print('Ola mundo')
print('Ola mundo')
del c
print('Ola mundo')
print('Ola mundo')
