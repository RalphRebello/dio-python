class Bicicleta:
    # metodo construtor e atributos da classe
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Plim Plim')

    def parar(self):
        print('Parando')
        print('Bicicleta parada')

    def correr(self):
        print('Vruuuuum...')

    # def __str__(self):
    #     return (f"Bicicleta: "
    #             f"cor: {self.cor}, "
    #             f"modelo: `{self.modelo}, "
    #             f"ano: {self.ano}, "
    #             f"valor: {self.valor}")

# mesma coisa que em cima, mas usando chamadas de metodos do python
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 189)
# igual a b2.buzinar()
Bicicleta.buzinar(b2)

print(b2)
