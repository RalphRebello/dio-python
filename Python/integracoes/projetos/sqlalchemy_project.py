from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Configuração da base declarativa
Base = declarative_base()


# Definição da tabela Cliente
class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(9), nullable=False, unique=True)
    endereco = Column(String, nullable=True)

    # Relação com a tabela Conta
    contas = relationship('Conta', back_populates='cliente')


# Definição da tabela Conta
class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id'))
    saldo = Column(Numeric(10, 2), nullable=False)

    # Relação com a tabela Cliente
    cliente = relationship('Cliente', back_populates='contas')


# Conectando ao banco de dados SQLite (em memória para este exemplo)
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Inserindo dados na tabela Cliente
cliente1 = Cliente(nome='João Silva', cpf='123456789', endereco='Rua A, 123')
cliente2 = Cliente(nome='Maria Souza', cpf='987654321', endereco='Rua B, 456')

session.add_all([cliente1, cliente2])
session.commit()

# Inserindo dados na tabela Conta
conta1 = Conta(tipo='Corrente', agencia='001', num=1234, id_cliente=cliente1.id, saldo=1000.50)
conta2 = Conta(tipo='Poupança', agencia='002', num=5678, id_cliente=cliente2.id, saldo=2500.75)

session.add_all([conta1, conta2])
session.commit()

# Recuperando informações de um cliente e suas contas
cliente = session.query(Cliente).filter_by(nome='João Silva').first()
print(f"Cliente: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}")
for conta in cliente.contas:
    print(f"Conta {conta.tipo}, Agência: {conta.agencia}, Número: {conta.num}, Saldo: R$ {conta.saldo}")

# Recuperando informações de todas as contas
contas = session.query(Conta).all()
for conta in contas:
    print(f"Conta ID: {conta.id}, Tipo: {conta.tipo}, Agência: {conta.agencia}, "
          f"Saldo: R$ {conta.saldo}, Cliente: {conta.cliente.nome}")

