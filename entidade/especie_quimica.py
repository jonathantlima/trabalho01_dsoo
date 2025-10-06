from abc import ABC, abstractmethod

class EspecieQuimica(ABC):

    @abstractmethod
    def __init__(self, nome: str, formula: str, funcao: str, valencia: int, coeficiente_de_difusao: float):
        self.__nome = nome
        self.__formula = formula
        self.__funcao = funcao
        self.__valencia = valencia
        self.__coeficiente_de_difusao = coeficiente_de_difusao
        self.__coeficiente_migracao_ionica = (self.__coeficiente_de_difusao * abs(self.__valencia) *\
                                              96485) / (8.3144 * 293.15)
        super().__init__()
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def formula(self):
        return self.__formula
    
    @formula.setter
    def formula(self, formula: str):
        if isinstance(formula, str):
            self.__formula = formula
    
    @property
    def funcao(self):
        return self.__funcao
    
    @funcao.setter
    def funcao(self, funcao: str):
        if isinstance(funcao, str):
            self.__funcao = funcao
    
    @property
    def coeficiente_de_difusao(self) -> float:
        return self.__coeficiente_de_difusao
    
    @coeficiente_de_difusao.setter
    def coeficiente_de_difusao(self, coeficiente_de_difusao: float):
        if isinstance(coeficiente_de_difusao, float):
            self.__coeficiente_de_difusao = coeficiente_de_difusao
