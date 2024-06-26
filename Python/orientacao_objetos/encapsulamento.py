class Conta:
    def __init__(self, n_ag, saldo=0):
        self._saldo = saldo # privado tem o _ na frente do nome
        self.n_ag = n_ag # publico não tem _ no começo do nome

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("001", 100)
# print(conta._saldo) mostra um alerta que a variavel é protegida
print(conta.n_ag)
conta.depositar(100)
print(conta.mostrar_saldo())
