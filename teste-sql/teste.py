from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

DATABASE_URL = "sqlite:///exemplo.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

engine = create_engine('sqlite:///biblioteca.db')
Session = sessionmaker(bind=engine)
session = Session()

class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    localizacao = Column(String(100))

    def __repr__(self):
        return f"<Departamento(id='{self.id}, 'nome='{self.nome}', localizacao='{self.localizacao}')>"

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    salario = Column(Integer)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    funcionario = relationship('Departamento', backref='funcionarios')

    def __repr__(self):
        return f"<Funcionario(nome='{self.autor}', email='{self.email}', salario='{self.salario}')>"
    
Base.metadata.create_all(engine)

def adicionar_departamento(nome, localizacao):
    departamento = session.query(Departamento).filter_by(nome=nome).first()
    if not departamento:
        departamento = Departamento(nome=nome, localizacao=localizacao)
        session.add(departamento)
        session.commit()

def visualizar_funcionario(nome):
    funcionario = session.query(Funcionario).filter_by(nome=nome).first()
    if not funcionario:
        print(f'Funcionario "{nome}" não encontrado.')
        return
    else:
        print(f'O Funcionario "{nome}" é do departamento: {funcionario}')

def adicionar_funcionario(nome, email, salario):
    funcionario = session.query(Funcionario).filter_by(nome=nome).first()
    if not funcionario:
        funcionario = Funcionario(nome=nome, email=email, salario=salario)
        session.add(funcionario)
        session.commit()
        print("Funcionário '{nome}' adicionado com sucesso")
        return

def consultar_departamentos():
    departamentos = session.query(Departamento).all()
    for departamento in departamentos:
        print(departamento.nome)

def consultar_funcionarios():
    funcionarios = session.query(Funcionario).all()
    for funcionario in funcionarios:
        print(funcionario.nome)

def main():
    while True:
        print('\nEscolha uma opção:')
        print('1. Adicionar Autor')
        print('2. Adicionar Livro')
        print('3. Consultar Livros')
        print('4. Consultar Autores')
        print('5. Sair')

        opcao = input('Opção: ')
        if opcao == '1':
            nome = input('Nome do Autor: ')
            adicionar_autor(nome)
        elif opcao == '2':
            titulo = input('Título do Livro: ')
            autor_nome = input('Nome do Autor: ')
            adicionar_livro(titulo, autor_nome)
        elif opcao == '3':
            consultar_livros()
        elif opcao == '4':
            consultar_autor()
        elif opcao == '5':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()