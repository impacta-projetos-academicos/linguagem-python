'''
(Referencia o diagrama na atividade)
O diagrama fornece uma hierarquia de classes onde a classe
Pessoa é a superclasse (classe mãe), e as classes
PessoaFisica e PessoaJuridica são as subclasses (classes
filhas).
Crie a classe Pessoa com os atributos identificador e nome.
Crie a classe PessoaJuridica que herda da classe Pessoa e
acrescenta o atributo CNPJ.
Crie a classe PessoaFisica que herda da classe Pessoa e
acrescenta os atributos RG e CPF.
'''

class Pessoa:
    def __init__(self, identificador, nome):
        self.identificador = identificador
        self.nome = nome

class PessoaJuridica(Pessoa):
    def __init__(self, identificador, nome, cnpj):
        super().__init__(identificador, nome)
        self.cnpj = cnpj
    
class PessoaFisica(Pessoa):
    def __init__(self, identificador, nome, rg, cpf):
        super().__init__(identificador, nome)
        self.rg  =  rg
        self.cpf = cpf

pessoa1 = Pessoa(1, "Jully")
p_juridica = PessoaJuridica(2, "Caetano", "11111111111")
p_fisica = PessoaFisica(3, "Joel","55555555555", "22222222222")

print("INFORMAÇÕES PESSOA")
print(pessoa1.identificador)
print(pessoa1.nome)
print("___________________\n")

print("INFORMAÇÕES PESSOA JURIDICA")
print(p_juridica.identificador)
print(p_juridica.nome)
print(p_juridica.cnpj)
print("___________________\n")

print("INFORMAÇÕES PESSOA FISICA")
print(p_fisica.identificador)
print(p_fisica.nome)
print(p_fisica.rg)
print(p_fisica.cpf)
print("___________________\n")