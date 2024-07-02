from sqlalchemy import *
from sqlalchemy.orm import *


Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship('Address', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship('User', back_populates='address')

    def __repr__(self):
        return f"Address(id={self.id}, email={self.email})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine)

insp = inspect(engine)
print(insp.has_table(table_name="user_account"))
print(insp.get_table_names())
print(insp.default_schema_name)

with Session(engine) as session:
    ralph = User(
        name='ralph',
        fullname='Ralph Rebello',
        address=[Address(email='ralph.rebello@gmail.com')]
    )

    hina = User(
        name='hina',
        fullname='Hina Araujo',
        address=[Address(email='hina_araujo@hotmail.com'),
                 Address(email='hina_silva@outlook.com')]
    )

    amelia = User(
        name='amelia',
        fullname='Amelia Araujo Rebello'
    )

    # enviando para o BD (persistencia de dados)
    session.add_all([ralph, hina, amelia])
    session.commit()

# como ver o statement
print(select(User).where(User.name.in_(['ralph', 'hina'])))

# exemplo de consulta no BD
stmt = select(User).where(User.name.in_(['ralph', 'hina']))
for user in session.scalars(stmt):
    print(user)

# consulta em usuario com 2 emails
stmt_address = select(Address).where(Address.user_id.in_([2]))
for address in session.scalars(stmt_address):
    print(address)

# consulta ordenada decrescente
stmt_order = select(User).order_by(User.fullname.desc())
for order in session.scalars(stmt_order):
    print(order)

# consulta ordenada crescente
stmt_order = select(User).order_by(User.fullname.asc())
for order in session.scalars(stmt_order):
    print(order)

# inner join
stmt_join = select(User.fullname, Address.email).join_from(Address, User)
for j in session.scalars(stmt_join):
    print(j)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
for j_all in results:
    print(j_all)

# count de instancias
stmt_count = select(func.count('*')).select_from(User)
for c in session.scalars(stmt_count):
    print(c)
