from numpy import arange, zeros
from entidade.anion import Anion
from entidade.cation import Cation
from entidade.condicao_inicial import CondicaoInicial
from entidade.condicao_de_contorno import CondicaoDeContorno


class Modelagem:

    def __init__(self,
                 condicao_inicial: CondicaoInicial,
                 condicao_de_contorno: CondicaoDeContorno,
                 space_increment: float = 0.5,
                 time_increment: float = 0.125
    ):
        if isinstance(condicao_inicial, CondicaoInicial):
            self.__condicao_inicial = condicao_inicial
        if isinstance(condicao_de_contorno, CondicaoDeContorno):
            self.__condicao_de_contorno = condicao_de_contorno
        if isinstance(space_increment, float):
            self.__space_increment = space_increment
        if isinstance(time_increment, float):
            self.__time_increment = time_increment
        self.__C = None

    @property
    def condicao_inicial(self) -> CondicaoInicial:
        return self.__condicao_inicial

    @property
    def condicao_de_contorno(self) -> CondicaoDeContorno:
        return self.__condicao_de_contorno

    @property
    def time_increment(self) -> float:
        return self.__time_increment

    @time_increment.setter
    def time_increment(self, time_increment: float):
        if isinstance(time_increment, float):
            self.__time_increment = time_increment

    @property
    def space_increment(self) -> float:
        return self.__space_increment

    @space_increment.setter
    def space_increment(self, space_increment: float):
        if isinstance(space_increment, float):
            self.__space_increment = space_increment

    def calcula_coeficientes(self):

        especie = self.__condicao_inicial.especie_quimica
       
        coeficiente_de_distribuicao = especie.coeficiente_de_distribuicao

        coeficiente_de_retardamento = 1. + (self.__simulacao.solo.massa_especifica_seca / self.__simulacao.solo.porosidade) *\
            coeficiente_de_distribuicao

        cte_p = (especie.coeficiente_de_difusao / coeficiente_de_retardamento) *\
                (self.__time_increment / (self.__space_increment ** 2))
        
        if isinstance(self.__condicao_inicial.especie_quimica, Cation):
            cte_r = ((especie.coeficiente_migracao_ionica + self.__simulacao.solo.permeabilidade_eletroosmotica) *\
                    (self.__time_increment * self.__condicao_inicial.gradiente_eletrico)) /\
                    (coeficiente_de_retardamento * 2 * self.__space_increment)

        elif isinstance(self.__condicao_inicial.especie_quimica, Anion):
            cte_r = ((self.__condicao_inicial.especie_quimica.coeficiente_de_migracao_ionica - self.__simulacao.solo.permeabilidade_eletroosmotica) *\
                    (self.__time_increment * self.__condicao_inicial.gradiente_eletrico)) /\
                    (coeficiente_de_retardamento * 2 * self.__space_increment)

        cte_s = (self.__simulacao.solo.condutividade_hidraulica * self.__time_increment * self.__condicao_inicial.gradiente_hidraulico) /\
                (coeficiente_de_retardamento * 2 * self.__space_increment)
        
        return coeficiente_de_retardamento, cte_p, cte_r, cte_s
    
    def cria_mesh(self):
        # discretiza a dimensão espaço
        space_array = arange(0, self.__simulacao.celula_experimental.comprimento +
                    self.__space_increment, self.__space_increment)

        # discretiza a dimensao do tempo
        time_array = arange(0, self.__simulacao.duracao + self.__time_increment, self.__time_increment)

        # calcula o número de linhas e colunas da matriz
        n = len(space_array)   # número de colunas
        m = len(time_array)   # número de linhas

        # inicializa a matriz de concentrações
        self.__C = zeros((m, n))

        return n, m, self.__C
    
    def aplica_condicoes(self):
         n, m, self.__C = self.cria_mash()
         CI = self.__condicao_inicial.concentracao_inicial

         inc = (CI[1] - CI[0]) / n   # calcula o incremento para o arange seguinte
         self.__C[0, :] = arange(CI[0], CI[1], inc)
         self.__C[:, 0] = self.__condicao_de_contorno.concentracao_reservatorio

         return self.__C
    
    def execucao(self):

        _, p, r, s = self.calcula_coeficientes()
        n, m, self.__C = self.cria_mesh()
        self.aplica_condicoes()

        
        for i in range(1, m):
            for j in range(1, n-1):
                self.__C[i,j] = (self.__C[i-1, j+1] * (p + r + s) +
                                 self.__C[i-1, j] * (-2 * p) +
                                 self.__C[i-1, j-1] * (p - r - s))

            # Condição de contorno no final
            self.__C[i, n-1] = self.__C[i-1, n-2]
        
        return self.__C
