from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)
session = Session()

metadata_obj = MetaData()
user = Table('user',
             metadata_obj,
             Column('user_id', Integer, primary_key=True),
             Column('user_name', String(40), nullable=False),
             Column('email_address', String(60)),
             Column('nickname', String(40), nullable=False))

user_prefs = Table('user_prefs', metadata_obj,
                   Column('pref_id', Integer, primary_key=True),
                   Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
                   Column('pref_name', String(40), nullable=False),
                   Column('pref_value', String(100)))

metadata_obj.create_all(engine)

for t in metadata_obj.sorted_tables:
    print(t)

metadata_db_obj = MetaData()
financial_info = Table('financial_info', metadata_db_obj,
                       Column('id', Integer, primary_key=True),
                       Column('value', String(100), nullable=False))

# prints da tabela financial info
print(financial_info.primary_key)
print(financial_info.constraints)
print('\n')
print(user_prefs.primary_key)
print(user_prefs.constraints)
print('\n')
print(metadata_obj.tables)
print('\n')

# usando consultas com sql
sql_insert = text('insert into user values(1, "ralph", "ralph.rebello@gmail.com", "kid")')
session.execute(sql_insert)

sql = text('select * from user')
result = session.execute(sql)
for row in result:
    print(row)


