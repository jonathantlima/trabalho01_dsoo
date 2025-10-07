from entidade.especie_quimica import EspecieQuimica

class Cation(EspecieQuimica):

    def __init__(self, nome: str, formula: str, funcao: str, valencia: int, coeficiente_de_difusao: float):
        super().__init__(nome, formula, funcao, coeficiente_de_difusao)