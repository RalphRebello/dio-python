class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


a1 = Estudante('Ralph', 12345)
a2 = Estudante('Hina', 54321)

mostrar_valores(a1, a2)

Estudante.escola = 'Python'

a1.matricula = 3

mostrar_valores(a1, a2)

a3 = Estudante('Amelia', 5678)

mostrar_valores(a1, a2, a3)
