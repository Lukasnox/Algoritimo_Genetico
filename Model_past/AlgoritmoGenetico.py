from Model_past.Individuo import Individuo

class AlgoritmoGenetico():
#----------------------------------------------------------------------------------
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
#----------------------------------------------------------------------------------
    def inicializa_populacao(self, espacos, valores, limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos, valores, limite_espacos))
        
        self.melhor_solucao = self.populacao[0]
#----------------------------------------------------------------------------------
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao, 
        key = lambda populacao: populacao.nota_avaliacao,
        reverse=True)
#----------------------------------------------------------------------------------
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avalaicao:
            self.melhor_solucao = individuo