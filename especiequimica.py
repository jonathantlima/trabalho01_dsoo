from abc import ABC, abstractmethod

class EspecieQuimica(ABC):
    @abstractmethod
    def __init__(self, nome: str, formula: str, tipo: str, coeficiente_de_difusao: float):
        if isinstance(nome,str):
            self.__nome = nome
        if isinstance(formula,str):
            self.__formula = formula
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(coeficiente_de_difusao, float):
            self.__coeficiente_de_difusao = coeficiente_de_difusao
        
    @property
    def nome(self)-> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def formula(self) -> str:
        return self.__formula
    
    @formula.setter
    def formula(self, formula: str):
        if isinstance(formula, str):
            self.__formula = formula

    @property
    def tipo(self)-> str:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    @property
    def coeficiente_de_difusao(self)-> float:
        return self.__coeficiente_de_difusao
    
    @coeficiente_de_difusao.setter
    def coeficiente_de_difusao(self, coeficiente_de_difusao: float):
        if isinstance(coeficiente_de_difusao, float):
            self.__coeficiente_de_difusao = coeficiente_de_difusao

    