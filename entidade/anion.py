from entidade.especie_quimica import EspecieQuimica

class Anion(EspecieQuimica):

    def __init__(self, nome: str, formula: str, funcao: str, valencia: int, coeficiente_de_difusao: float):
        super().__init__(nome, formula, funcao, valencia, coeficiente_de_difusao)