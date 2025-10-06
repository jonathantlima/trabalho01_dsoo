from entidade.solo import Solo

class Silte(Solo):

    def __init__(self,
                 tipo,
                 origem,
                 cor,
                 porosidade,
                 massa_especifica_seca,
                 condutividade_hidraulica,
                 permeabilidade_eletroosmotica
    ):
        super().__init__(tipo,
                         origem,
                         cor,
                         porosidade,
                         massa_especifica_seca,
                         condutividade_hidraulica,
                         permeabilidade_eletroosmotica
        )