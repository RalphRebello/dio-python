import hashlib

string = input('Informe o texto para gerar o hash -> ')

menu =  int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ####
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    
                    Digite o numero para escolher o tipo do hash a ser gerado -> '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print(f'Hash MD5 da string é {result.hexdigest()}')
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print(f'Hash SHA1 da string é {result.hexdigest()}')
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print(f'Hash SHA256 da string é {result.hexdigest()}')
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print(f'Hash SHA512 da string é {result.hexdigest()}')
else:
    print('Opção invalida, tente novamente')
