def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * b + b * 3

def resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado é {resultado}")

resultado(1, 2, somar)
resultado(1, 2, subtrair)
resultado(1, 2, test)

#é possivel atribuir a funcao a uma variavel
op = somar
print(op(1, 2))