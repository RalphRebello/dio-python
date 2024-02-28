#def exemplo(arg1, arg2 / agr3, arg4 * arg5, arg6)
#argumentos antes da '/' são por posição
#argumentos entre a '/' e o '*' pode ser por posição ou por chave: valor
#argumentos depois do '*' são apenas por chave: valor
#não é necessário usar os dois '/' e '*'

def cria_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    # salva no banco de dados
    print(modelo, ano, placa, marca, motor, combustivel)

cria_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina")
cria_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
