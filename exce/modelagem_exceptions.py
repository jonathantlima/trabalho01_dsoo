from .erro_sistema_exception import ErroSistemaException

class FaltaCondicaoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Falta de CondicaoInicial ou CondicaoDeContorno na modelagem.")

class ErroCalculoNumericoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro de cálculo numérico (overflow, NaN, divisão por zero).")

class ErroSalvarModelagemException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro ao salvar ou carregar o modelo.")

class ModelagemAssociadaInexistenteException(ErroSistemaException):
    def __init__(self):
        super().__init__("Modelagem associada a simulação inexistente.")