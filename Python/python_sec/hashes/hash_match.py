import hashlib


a1 = 'a.txt'
a2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(a1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(a2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {a1} é diferente do arquivo {a2}')
    print(f'hash de {a1} -> {hash1.hexdigest()}')
    print(f'hash de {a2} -> {hash2.hexdigest()}')
else:
    print(f'O arquivo {a1} é igual do arquivo {a2}')
    print(f'hash de {a1} -> {hash1.hexdigest()}')
    print(f'hash de {a2} -> {hash2.hexdigest()}')
