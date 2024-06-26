class Animal:
    def __init__(self, qtd_patas):
        self.qtd_patas = qtd_patas

    def __str__(self):
        return (f'{self.__class__.__name__}: '
                f'{", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}')


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico


class Cachorro(Mamifero):
    pass


class Gato(Mamifero):
    pass


class Leao(Mamifero):
    pass


class FalarMixin:
    def falar(self):
        return 'oi estou falastrao'


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, qtd_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, qtd_patas=qtd_patas)
        print(Ornitorrinco.__mro__) # ordem da busca nas classes


gato = Gato(qtd_patas=4, cor_pelo='preto')
print(gato)

ornitorrinco = Ornitorrinco(qtd_patas=2, cor_pelo='marrom', cor_bico='laranja')
print(ornitorrinco)
print(ornitorrinco.falar())
