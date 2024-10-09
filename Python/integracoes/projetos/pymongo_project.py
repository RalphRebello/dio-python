from pymongo import MongoClient

# URL de conexão do MongoDB Atlas (substitua com sua própria URI)
# Obtenha isso no painel do MongoDB Atlas
MONGO_URI = "mongodb+srv://<usuário>:<senha>@cluster0.mongodb.net/test?retryWrites=true&w=majority"

# Conectar ao MongoDB Atlas
client = MongoClient(MONGO_URI)

# Acessar/criar banco de dados
db = client['banco']

# Acessar/criar coleções (equivalente a tabelas)
clientes_collection = db['clientes']
contas_collection = db['contas']

# Inserir documentos (equivalente a linhas nas tabelas)
cliente1 = {
    "nome": "João Silva",
    "cpf": "123456789",
    "endereco": "Rua A"
}

cliente2 = {
    "nome": "Maria Oliveira",
    "cpf": "987654321",
    "endereco": "Rua B"
}

# Inserir clientes
clientes_collection.insert_many([cliente1, cliente2])

# Recuperar IDs dos clientes inseridos para vincular com as contas
joao = clientes_collection.find_one({"cpf": "123456789"})
maria = clientes_collection.find_one({"cpf": "987654321"})

# Inserir contas associadas aos clientes
conta1 = {
    "tipo": "Corrente",
    "agencia": "001",
    "num": 12345,
    "saldo": 1500.00,
    "id_cliente": joao["_id"]
}

conta2 = {
    "tipo": "Poupança",
    "agencia": "002",
    "num": 54321,
    "saldo": 3000.00,
    "id_cliente": maria["_id"]
}

# Inserir contas
contas_collection.insert_many([conta1, conta2])

# Recuperação de dados

# Listar todos os clientes
clientes = clientes_collection.find()
print("Clientes:")
for cliente in clientes:
    print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Endereço: {cliente['endereco']}")

# Listar todas as contas e os respectivos clientes
contas = contas_collection.find()
print("\nContas:")
for conta in contas:
    cliente = clientes_collection.find_one({"_id": conta['id_cliente']})
    print(f"Conta {conta['num']} do cliente {cliente['nome']}, Agência: {conta['agencia']}, Saldo: {conta['saldo']}")

# Buscar cliente específico pelo CPF
cpf_busca = '123456789'
cliente_encontrado = clientes_collection.find_one({"cpf": cpf_busca})
if cliente_encontrado:
    print(f"\nCliente encontrado: {cliente_encontrado['nome']}, Endereço: {cliente_encontrado['endereco']}")
