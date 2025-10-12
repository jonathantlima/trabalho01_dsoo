from .erro_sistema_exception import ErroSistemaException

class ParametrosFisicosInvalidosException(ErroSistemaException):
    def __init__(self):
        super().__init__("Parâmetros físicos inválidos (ex.: duração negativa, solo nulo).")

class CondicoesIniciaisIncompativeisException(ErroSistemaException):
    def __init__(self):
        super().__init__("Condições iniciais incompatíveis com o tipo de simulação.")

class EspecieQuimicaInexistenteException(ErroSistemaException):
    def __init__(self):
        super().__init__("Espécie química não definida na simulação.")

class ErroUnidadeException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro de unidade — valores fora da faixa esperada (ex.: concentração < 0).")

class ErroGerarRelatorioException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro ao gerar relatório de simulação.")