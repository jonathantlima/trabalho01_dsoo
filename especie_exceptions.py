from .erro_sistema_exception import ErroSistemaException

class NomeDuplicadoEspecieException(ErroSistemaException):
    def __init__(self, nome=""):
        super().__init__(f"Nome duplicado de espécie: {nome}")

class CoeficienteDifusaoNegativoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Coeficiente de difusão negativo.")

class ErroTipoDadoEspecieException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro de tipo de dado (ex.: fórmula química inválida).")

class EspecieSemPropriedadesException(ErroSistemaException):
    def __init__(self):
        super().__init__("Espécie sem propriedades obrigatórias definidas.")