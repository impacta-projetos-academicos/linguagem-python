from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from contextlib import contextmanager

DATABASE_URL = "sqlite:///exemplo.db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

engine = create_engine('sqlite:///biblioteca.db')
SessionLocal = sessionmaker(bind=engine)
session = Session()

class Departamento(Base):
    __tablename__ = 'departamentos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    localizacao = Column(String(100))
    
    funcionarios = relationship("Funcionario", back_populates="departamento")

    def __repr__(self):
        return f"<Departamento(id='{self.id}, 'nome='{self.nome}', localizacao='{self.localizacao}')>"

class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    salario = Column(Integer)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    
    departamento = relationship('Departamento', back_populates='funcionarios')

    def __repr__(self):
        return f"<Funcionario(nome='{self.autor}', email='{self.email}', salario={self.salario}, departamento={self.departamento.nome if self.departamento else 'Nenhum'})>"

def criar_banco():
    Base.metadata.create_all(engine)
    print("Banco criado.")

def adicionar_departamento(nome, localizacao=None):
    departamento = session.query(Departamento).filter_by(nome=nome).first()
    if not departamento:
        departamento = Departamento(nome=nome, localizacao=localizacao)
        session.add(departamento)
        session.commit()
        print(f"Departamento: {nome} foi adicionado!")
    else:
        print(f"Departamento já existe.")

def visualizar_funcionario(nome):
    funcionario = session.query(Funcionario).filter_by(nome=nome).first()
    if not funcionario:
        print(f'Funcionario "{nome}" não encontrado.')
        return
    else:
        print(f'O Funcionario "{nome}" é do departamento: {funcionario}')
        # não sei como acessar o departamento do funcionário

def adicionar_funcionario(nome, email, salario, departamento_nome):
    funcionario = session.query(Funcionario).filter_by(nome=nome).first()
    if not funcionario:
        funcionario = Funcionario(nome=nome, 
                                  email=email, 
                                  salario=salario,
                                  departamento = departamento_nome
                                  )
        session.add(funcionario)
        session.commit()
        print("Funcionário '{nome}' adicionado com sucesso")
        return funcionario
    else:
        print(f"Funcionário '{nome}' já existe")
    
def consultar_departamentos():
    departamentos = session.query(Departamento).all()
    if not departamentos:
        print("Nenhum departamento cadastrado.")
    else:
        print("\nDepartamentos:")
        for i, depto in enumerate(departamentos, 1):
            print(f"{i}. {depto.nome} ({depto.localizacao}) - {len(depto.funcionarios)} funcionários")

def consultar_funcionarios():
    funcionarios = session.query(Funcionario).all()
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nFuncionários:")
        for i, func in enumerate(funcionarios, 1):
            print(f"{i}. {func.nome} - {func.email} - R${func.salario} - Depto: {func.departamento.nome if func.departamento else 'Nenhum'}")

def main():
    criar_banco()
    
    adicionar_departamento("TI", "Andar 5")
    adicionar_departamento("RH", "Andar 2")
    adicionar_funcionario("João Silva", "joao@empresa.com", 5000, "TI")
    adicionar_funcionario("Maria Souza", "maria@empresa.com", 6000, "TI")
    adicionar_funcionario("Carlos Mendes", "carlos@empresa.com", 4500, "RH")
    
    while True:
        print('\n=== MENU PRINCIPAL ===')
        print('1. Adicionar Departamento')
        print('2. Adicionar Funcionário')
        print('3. Consultar Funcionário')
        print('4. Consultar Departamentos')
        print('5. Consultar Funcionários')
        print('6. Sair')

        opcao = input('\nOpção: ').strip()
        
        if opcao == '1':
            nome = input('Nome do departamento: ').strip()
            localizacao = input('Localização (opcional): ').strip() or None
            adicionar_departamento(nome, localizacao)
        
        elif opcao == '2':
            nome = input('Nome do funcionário: ').strip()
            email = input('Email do funcionário: ').strip()
            salario = int(input('Salário do funcionário: ').strip())
            depto = input('Departamento (opcional): ').strip() or None
            adicionar_funcionario(nome, email, salario, depto)
        
        elif opcao == '3':
            nome = input('Nome do funcionário a consultar: ').strip()
            visualizar_funcionario(nome)
        
        elif opcao == '4':
            consultar_departamentos()
        
        elif opcao == '5':
            consultar_funcionarios()
        
        elif opcao == '6':
            print("Saindo do sistema...")
            session.close()
            break
        
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()