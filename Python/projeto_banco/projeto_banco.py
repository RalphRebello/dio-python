def listar_usuarios(usuarios):

    for cpf, dados in usuarios.items():
        print("\nCPF:", cpf)
        print("Nome:", dados["nome"])
        print("Data de Nascimento:", dados["data_nascimento"])
        print(f"Endereço: "
              f"{dados['endereco']['rua']}, "
              f"{dados['endereco']['numero']} - "
              f"{dados['endereco']['bairro']} - "
              f"{dados['endereco']['cidade']}/"
              f"{dados['endereco']['estado']}")

def cria_conta():
    print()

def cria_usuario():
    novo_usuario = {}

    nome = input("Informe o nome -> ").title()
    cpf = input("Informe o CPF -> ").replace(".", "").replace("-", "")
    data_nascimento = str(input(f"Dia, mês e ano com 4 numeros -> ")).replace(" ", "/")
    
    print("Informe o endereço: ")
    endereco = {
        "rua": input("Rua -> ").title(),
        "numero": input("Número -> "),
        "bairro": input("Bairro -> ").title(),
        "cidade": input("Cidade -> ").title(),
        "estado": input("Estado (sigla) -> ").upper()
    }

    novo_usuario = {
        cpf: {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco
        }
    }
    
    print("\nUsuário cadastrado com sucesso!")
    listar = bool(input("\nDeseja conferir os dados do usuário cadastrado? 1-sim | 0-não -> "))

    if listar == True:
        listar_usuarios(novo_usuario)

    return novo_usuario

def depositar(saldo, valor, extrato):
    print('\nDepósito')
    
    extrato.append('Dep | R$' + str(valor))
    saldo += valor
    print('\nDepósito efetuado com sucesso!')

    return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    print('\nSaque')
    if saldo > 0:
        if numero_saques < limite_saques:
            if saldo - valor >= 0 and valor <= limite:
                extrato.append('Saq | -R$' + str(valor))
                saldo -= valor
                numero_saques += 1
                print('Saque efetuado com sucesso!')
            else:
                print('Valor do valor não permitido')
        else:
            print('Limite de saques excedido, tente novamente amanhã')
    else:
        print('Saldo insuficiente!')
    
    return saldo, extrato


def gera_extrato(saldo, *, extrato):
    print('\nExtrato')
    for op in extrato:
        if str(op).startswith('Saq'):
            print('\033[91m' + op + '\033[0m')  # print red
        else:
            print(op)
    print(f'Saldo atual => R${saldo:.2f}')


def main():

    valor = 0
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    usuarios = {}

    menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Ciar usuário
    [q] Sair

    => '''

    while True:
        opcao = input(menu)

        if opcao == 'd':
            valor = abs(float(input('informe o valor do depósito => ')))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = abs(float(input('informe o valor do saque => ')))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, 
                                   limite=limite, numero_saques=numero_saques, 
                                   limite_saques=LIMITE_SAQUES)
        
        elif opcao == 'e':
            gera_extrato(saldo, extrato=extrato)
    
        elif opcao == 'c':
            usuarios.update(cria_usuario())

        elif opcao == 'q':
            listar_usuarios(usuarios)
            print('Saindo')
            break
        
        else:
            print('Opção inválida!')
            print('Tente novamente')
main()
