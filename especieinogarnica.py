from especiequimica import EspecieQuimica

class EspecieInorganica(EspecieQuimica):
    def __init__(self, nome: str, formula: str, tipo: str, coeficiente_de_difusao: float):
        super().__init__(nome, tipo, formula, coeficiente_de_difusao)
        if isinstance(nome,str):
            self.__nome = nome
        if isinstance(formula,str):
            self.__formula = formula
        if isinstance(tipo, str):
            self.__tipo = tipo
        if isinstance(coeficiente_de_difusao, float):
            self.__coeficiente_de_difusao = coeficiente_de_difusao
        