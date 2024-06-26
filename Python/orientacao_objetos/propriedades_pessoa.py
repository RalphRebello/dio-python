class Pessoa:
    def __init__(self, nome, ano_nasc):
        self.nome = nome
        self._ano_nasc = ano_nasc

    @property
    def idade(self):
        return 2024 - self._ano_nasc


pessoa = Pessoa('ralph', 1992)
print(f'{str(pessoa.nome).title()} | {pessoa.idade} anos')
