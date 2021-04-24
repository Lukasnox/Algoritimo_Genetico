from Model_past.Individuo import Individuo
from Model_past.Produto_class import Produto
from Model_past.AlgoritmoGenetico import AlgoritmoGenetico
#-----------------------------↑ Importando ↑---------------------------------------

if __name__ == '__main__':
#-----------------------------↓ Adicionando ↓--------------------------------------

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

    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append( produto.valor)
        nomes.append(produto.nome)
    
    limite = 3

#-----------------------------↓ Exibindo ↓------------------------------------------

    

    tamanho_populacao = 20
    ag = AlgoritmoGenetico(tamanho_populacao)
    ag.inicializa_populacao(espacos,valores,limite)

    for individuo in ag.populacao:
        individuo.avaliacao()
   
    ag.ordena_populacao()
    ag.melhor_individuo(ag.populacao[0])
    

    print(f'Melhor Solucao: {ag.melhor_solucao.cromossomo}',
    f'Nota - {ag.melhor_solucao.nota_avaliacao}')
    print("-------------------------------------------------------------------\n")


