'''
Crie a classe Imovel, que possui um endereço e um preço.
Crie a classe ImovelNovo, que herda de Imovel e possui um
adicional no preço.
Crie a classe ImovelVelho, que herda de Imovel e possui um
desconto no preço.
O método calcular_preco das classes deve retornar o preço
atualizado de acordo com o adicional ou desconto.
'''

class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco_imovel = preco
        
    @property
    def preco_imovel(self):
        return self._preco
    
    @preco_imovel.setter
    def preco_imovel(self, valor):
        while valor < 0:
            valor = float(input("O preço não pode ser negativo. Novo Preço: "))
        self._preco = valor
        
    def calcular_preco(self):
        return self._preco 

class ImovelNovo(Imovel):
    def __init__(self, endereco, preco, adicional_preco):
        super().__init__(endereco, preco)
        self.adicional_preco = adicional_preco
        
    def calcular_preco(self):
        if self.adicional_preco > 0:
            return self._preco + self.adicional_preco
        else:
            print("O adicional não pode ser negativo.")

class ImovelVelho(Imovel):
    def __init__(self, endereco, preco, desconto_preco):
        super().__init__(endereco, preco)
        self.desconto_preco = desconto_preco
        
    def calcular_preco(self):
        if self.desconto_preco > 0:
            return self._preco - self.desconto_preco
        else:
            print("O desconto não pode ser negativo.")
            
    def exibir_novo_preco(self):
        print("")
            
imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = ImovelNovo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = ImovelVelho("Av. Brasil, 777", 500000.0, 35000.0)

print("IMOVEL")
print(imovel.endereco)
print('Preço:', imovel.preco_imovel) 
print("___________________\n")

print("IMOVEL NOVO")
print(imovel_novo.endereco) 
print('Preço:', imovel_novo.preco_imovel)
print('Preço Atualizado:', imovel_novo.calcular_preco())
print("___________________\n")

print("IMOVEL VELHO")
print(imovel_velho.endereco) 
print('Preço:', imovel_velho.preco_imovel) 
print('Preço Atualizado:', imovel_velho.calcular_preco())
print("___________________\n")
