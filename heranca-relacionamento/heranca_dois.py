'''
Crie a classe Animal com os atributos nome, cor e
numero_patas. Crie também o método exibir_dados, que
imprime na tela os dados do animal (nome, cor e
numero_patas).

Crie a classe Cachorro que herda da classe Animal e que
possui como atributo adicional a raça do cachorro. Crie também
o método exibir_dados, que imprime na tela os dados do
cachorro (nome, cor, numero_patas e raca)
'''

class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor =  cor
        self.numero_patas = numero_patas
        
    def exibir_dados(self):
        print(f'NOME: {self.nome}\nCOR: {self.cor}\nNUMERO DE PATAS: {self.numero_patas}')
    
class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca):
        super().__init__(nome, cor, numero_patas)
        self.raca = raca
        
    def exibir_dados(self):
        print(f'NOME: {self.nome}\nCOR: {self.cor}\nNUMERO DE PATAS: {self.numero_patas}\nRAÇA: {self.raca}')

animal = Animal("Passaro", "Verde", 2)
animal.exibir_dados()
print("___________________\n")

cachorro_um = Cachorro("Narizinho", "Preto", 4, "Bulldog")
cachorro_um.exibir_dados()
print("___________________\n")
        