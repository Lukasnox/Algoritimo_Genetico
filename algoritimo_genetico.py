#------------------------↓Imports↓---------------------------------------------
from random import random

#---------------------------------------------------------------------
class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
#---------------------------------------------------------------------
class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0 #somatorio dos valores da carga
        self.espaco_usado = 0 #somatorio dos espaços da carga
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(len(espacos)):
            if random() < 0.5:
                self.cromossomo.append("0")
            else:
                self.cromossomo.append("1")
#---------------------------------------------------------------------             
    def avaliacao(self):
        nota = 0
        soma_espacos = 0
        for i in range(len(self.cromossomo)):
            if self.cromossomo[i] == '1':
                nota += self.valores[i]
                soma_espacos += self.espacos[i]
        if soma_espacos > self.limite_espacos:
            nota = 1
        self.nota_avaliacao = nota
        self.espaco_usado = soma_espacos
#---------------------------------------------------------------------        
    def crossover(self, outro_individuo):
        corte = round(random() * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
               Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
                
#---------------------------------------------------------------------

    def mutacao(self, taxa_mutacao):
        print(f"Antes {self.cromossomo}")
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == '1':
                    self.cromossomo[i] = '0'
                else:
                    self.cromossomo[i] = '1'
        print(f"Depois {self.cromossomo}")
        return self    

#---------------------------------------------------------------------  
#---------------------------------------------------------------------  
#------------------------↓Input↓---------------------------------------------
if __name__ == '__main__':   
    
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    
    espacos = []
    valores = []
    nomes = []
    limite = 3
    
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    
#------------------------↓Output↓---------------------------------------------
    
    print('\n')    

    individuo1 = Individuo(espacos, valores, limite)
    print("individuo - 1")
    for i in range(len(lista_produtos)):
        if individuo1.cromossomo[i] == "1":
            print(f'Nome: {lista_produtos[i].nome} / R$ {lista_produtos[i].valor}')
            
    individuo1.avaliacao()
    print(f'Nota = {individuo1.nota_avaliacao}')
    print(f'Espaço Usado = {individuo1.espaco_usado}')
    
    print('\n')
    
    individuo2 = Individuo(espacos, valores, limite)
    print("individuo - 2")
    for i in range(len(lista_produtos)):
        if individuo2.cromossomo[i] == "1":
            print(f'Nome: {lista_produtos[i].nome} / R$ {lista_produtos[i].valor}')
            
    individuo2.avaliacao()
    print(f'Nota = {individuo2.nota_avaliacao}')
    print(f'Espaço Usado = {individuo2.espaco_usado}')
            
    individuo1.crossover(individuo2)
    
    
    print('\nIndividuo 1')
    individuo1.mutacao(0.05)
    
    print('\nIndividuo 2')
    individuo2.mutacao(0.05)
            
            
            
            
            
            
            
            
            