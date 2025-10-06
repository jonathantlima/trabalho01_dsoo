from entidade.solo import Solo

class Argila(Solo):

    def __init__(self,
                 tipo: str,
                 origem: str,
                 cor: str,
                 porosidade: float,
                 massa_especifica_seca: float,
                 condutividade_hidraulica: float,
                 permeabilidade_eletroosmotica: float
    ):
        super().__init__(tipo,
                         origem,
                         cor,
                         porosidade,
                         massa_especifica_seca,
                         condutividade_hidraulica,
                         permeabilidade_eletroosmotica
        )
