from .erro_sistema_exception import ErroSistemaException

class TipoSoloInvalidoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Tipo de solo inválido ou desconhecido.")

class ParametrosFisicosIncoerentesException(ErroSistemaException):
    def __init__(self):
        super().__init__("Parâmetros físicos incoerentes (ex.: densidade negativa, porosidade > 1).")

class ErroCalculoPropriedadesException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro de cálculo de propriedades derivadas (ex.: divisão por zero).")