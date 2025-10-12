from datetime import date
from entidade.solo import Solo
from entidade.areia import Areia
from entidade.silte import Silte
from entidade.argila import Argila
from entidade.modelagem import Modelagem
from entidade.condicao_inicial import CondicaoInicial
from entidade.celula_experimental import CelulaExperimental

class Simulacao():

    def __init__(self,
                 data: date,
                 solo: Solo,
                 celula_experimental: CelulaExperimental,
                 modelo: Modelagem,
                 duracao: float = 24.
    ):
        if isinstance(data, date):
            self.__data = data
        if isinstance(solo, Solo):
            self.__solo = solo
        if isinstance(celula_experimental, CelulaExperimental):
            self.__celula_experimental = celula_experimental
        if isinstance(modelo, Modelagem):
            self.__modelo = modelo
        if isinstance(duracao, (int, float)):
            self.__duracao = float(duracao)
    
    @property
    def data(self) -> date:
        return self.__data
    
    @data.setter
    def data(self, data: date):
        if isinstance(data, date):
            self.__data = data
    
    @property
    def solo(self) -> Solo:
        return self.__solo
    
    @solo.setter
    def solo(self, solo: Solo):
        if isinstance(solo, Solo):
            self.__solo = solo
    
    @property
    def celula_experimental(self):
        return self.__celula_experimental
    
    @celula_experimental.setter
    def celula_experimental(self, celula_experimental: CelulaExperimental):
        if isinstance(celula_experimental, CelulaExperimental):
            self.__celula_experimental = celula_experimental
    
    @property
    def modelo(self) -> Modelagem:
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo: Modelagem):
        if isinstance(modelo, Modelagem):
            self.__modelo = modelo
    
    @property
    def duracao(self) -> float:
        return self.__duracao
    
    @duracao.setter
    def duracao(self, duracao: float):
        if isinstance(duracao, (int, float)):
            self.__duracao = duracao
