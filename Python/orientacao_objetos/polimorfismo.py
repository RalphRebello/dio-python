class Passaro:
    def voar(self):
        print('voando')


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        print('não pode voar')


class Aviao(Passaro):
    def voar(self):
        print('avião tbm voa')


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()
a1 = Aviao()

plano_voo(p1)
plano_voo(p2)
plano_voo(a1)
