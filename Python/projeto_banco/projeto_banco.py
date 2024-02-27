menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo
    print('\nDepósito')
    deposito = abs(float(input('informe o valor do depósito => ')))
    extrato.append('Dep | R$' + str(deposito))
    saldo += deposito
    print('\nDepósito efetuado com sucesso!')

def sacar():
    global saldo, numero_saques
    print('\nSaque')
    if saldo > 0:
        if numero_saques < LIMITE_SAQUES:
            saque = abs(float(input('informe o valor do saque => ')))
            if saldo - saque >= 0 and saque <= 500:
                extrato.append('Saq | -R$' + str(saque))
                saldo -= saque
                numero_saques += 1
                print('Saque efetuado com sucesso!')
            else:
                print('Valor do saque não permitido')
        else:
            print('Limite de saques excedido, tente novamente amanhã')
    else:
        print('Saldo insuficiente!')

def extrato():
    print('\nExtrato')
    for op in extrato:
        if str(op).startswith('Saq'):
            print('\033[91m' + op + '\033[0m')  # print red
        else:
            print(op)
    print(f'Saldo atual => R${saldo:.2f}')

while True:
    opcao = input(menu)

    if opcao == 'd':
        depositar()
    elif opcao == 's':
        sacar()
    elif opcao == 'e':
        extrato()
    elif opcao == 'q':
        print('Saindo')
        break
    else:
        print('Opção inválida!')
        print('Tente novamente')
