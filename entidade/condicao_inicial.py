from entidade.especie_quimica import EspecieQuimica
from entidade.cation import Cation
from entidade.anion import Anion

class CondicaoInicial:

    def __init__(self,
                 gradiente_eletrico: float,
                 gradiente_hidraulico: float,
                 especie_quimica: EspecieQuimica,
                 concentracao_inicial: list[float]
    ):
        if isinstance(gradiente_eletrico, float):
            self.__gradiente_eletrico = gradiente_eletrico
        if isinstance(gradiente_hidraulico, float):
            self.__gradiente_hidraulico = gradiente_hidraulico
        if isinstance(especie_quimica, EspecieQuimica):
            self.__especie_quimica = especie_quimica
        if isinstance(concentracao_inicial, list) and all(isinstance(v, (int, float)) for v in concentracao_inicial):
            self.__concentracao_inicial = concentracao_inicial
    
    @property
    def gradiente_eletrico(self) -> float:
        return self.__gradiente_eletrico
    
    @gradiente_eletrico.setter
    def gradiente_eletrico(self, gradiente_eletrico: float):
        if isinstance(gradiente_eletrico, float):
            self.__gradiente_eletrico = gradiente_eletrico
    
    @property
    def gradiente_hidraulico(self) -> float:
        return self.__gradiente_hidraulico
    
    @gradiente_hidraulico.setter
    def gradiente_hidraulico(self, gradiente_hidraulico: float):
        if isinstance(gradiente_hidraulico, float):
            self.__gradiente_hidraulico = gradiente_hidraulico
    
    @property
    def especie_quimica(self) -> EspecieQuimica:
        return self.__especie_quimica
    
    @especie_quimica.setter
    def especie_quimica(self, especie_quimica):
        if isinstance(especie_quimica, EspecieQuimica):
            self.__especie_quimica = especie_quimica
    
    @property
    def concentracao_inicial(self):
        return self.__concentracao_inicial
    
    @concentracao_inicial.setter
    def concentracao_inicial(self, valores):
        if isinstance(valores, list):
            self.__concentracao_inicial = valores
