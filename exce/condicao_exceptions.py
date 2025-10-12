from .erro_sistema_exception import ErroSistemaException

class EspecieQuimicaNaoDefinidaException(ErroSistemaException):
    def __init__(self):
        super().__init__("Espécie química não definida no domínio.")

class ValoresIniciaisForaIntervaloException(ErroSistemaException):
    def __init__(self):
        super().__init__("Valores iniciais fora do intervalo físico.")

class GradienteConcentracaoIndefinidoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Gradiente de concentração indefinido.")

class FalhaAssociacaoModelagemException(ErroSistemaException):
    def __init__(self):
        super().__init__("Falha na associação entre condição e modelagem.")