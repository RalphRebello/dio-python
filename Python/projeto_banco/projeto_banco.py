def criar_conta(usuarios, contas):
    cpf_usuario = input("Informe o CPF -> ").replace(".", "").replace("-", "")
    if usuarios.get(cpf_usuario):
        contas.append([cpf_usuario, "0001", str(len(contas) + 1)])
        print("Conta criada")
    else:
        print("CPF não cadastrado")

    print(contas)
    return contas


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


def valida_cpf_existente(usuarios):
    cpf = input("Informe o CPF -> ").replace(".", "").replace("-", "")

    if cpf in usuarios.keys():
        print("Usuario já cadastrado")
    else:
        usuarios.update(cria_usuario(cpf))

    return usuarios


def cria_usuario(cpf):
    nome = input("Informe o nome -> ").title()

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

    if listar:
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
    limite_saques = 3

    usuarios = {}
    contas = []

    menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Ciar usuário
    [c] Criar conta corrente
    [q] Sair

    => '''

    while True:
        opcao = input(menu)

        # depositar
        if opcao == 'd':
            valor = abs(float(input('informe o valor do depósito => ')))
            saldo, extrato = depositar(saldo, valor, extrato)
        # sacar
        elif opcao == 's':
            valor = abs(float(input('informe o valor do saque => ')))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato,
                                   limite=limite, numero_saques=numero_saques,
                                   limite_saques=limite_saques)
        # extrato
        elif opcao == 'e':
            gera_extrato(saldo, extrato=extrato)
        # criar novo usuario
        elif opcao == 'u':
            valida_cpf_existente(usuarios)
        # criar conta
        elif opcao == 'c':
            contas = criar_conta(usuarios, contas)
        # sair do programa
        elif opcao == 'q':
            listar_usuarios(usuarios)
            print('Saindo')
            break

        else:
            print('Opção inválida!')
            print('Tente novamente')


main()
