from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('ligando tv')

    def desligar(self):
        print('desligando tv')

    @property
    def marca(self):
        return 'LG'


class ControleAr(ControleRemoto):
    def ligar(self):
        print('ligando ar')

    def desligar(self):
        print('desligando ar')

    @property
    def marca(self):
        return 'MIDEA'


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = ControleAr()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)
