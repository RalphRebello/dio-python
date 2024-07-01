class Pessoa:
    def __init__(self, nome=None, idade=0):
        self.nome = nome
        self.idade = idade

    @classmethod
    def pessoa_nasc(cls, ano, nome):
        print(cls)
        idade = 2024 - ano
        return Pessoa(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18



p = Pessoa('Juca', 10)
print(p.nome, p.idade)

p2 = Pessoa.pessoa_nasc(1992, 'ralph')
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(p.idade))
print(Pessoa.maior_idade(p2.idade))
