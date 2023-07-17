from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/cinema").connect()
Base = declarative_base() # Mapeamento declarativo
Session = sessionmaker(bind=engine) # session baseado/vinculado/bind  nas conexões do bd
session = Session()

# Entidades
class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme (titulo={self.titulo}, ano={self.ano})'
    
# SQL

# Select

# data = session.query(Filmes).all()
# print(data)
# print(data[0].titulo)
'''
[Filme (titulo=Forest Gump, ano=1994), Filme (titulo=Titanic, ano=2001)]

Forest Gump
'''

#  Insert

# data_insert = Filmes(titulo='Batman', genero='Drama', ano=2022)
# session.add(data_insert)
# session.commit()
'''
[Filme (titulo=Batman, ano=2022), Filme (titulo=Forest Gump, ano=1994), Filme (titulo=Titanic, ano=2001)]
'''

#  Delete

# session.query(Filmes).filter(Filmes.titulo=='Titanic').delete()
# session.commit()
# [Filme (titulo=Batman, ano=2022), Filme (titulo=Forest Gump, ano=1994)]

# 1st
# data_insert = Filmes(titulo='endless love', genero='Drama', ano=1990)
# session.add(data_insert)
# session.commit()
# [Filme (titulo=Batman, ano=2022), Filme (titulo=endless love, ano=1990), Filme (titulo=Forest Gump, ano=1994)]

#  Update

session.query(Filmes).filter(Filmes.genero=='Drama').update({'ano': 2000})
session.commit()
#  [Filme (titulo=Batman, ano=2000), Filme (titulo=endless love, ano=2000), Filme (titulo=Forest Gump, ano=2000)]

data = session.query(Filmes).all()
print(data)
session.close()