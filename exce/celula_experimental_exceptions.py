from .erro_sistema_exception import ErroSistemaException

class DadosMedicaoInvalidosException(ErroSistemaException):
    def __init__(self):
        super().__init__("Dados de medição ausentes ou inválidos.")

class AssociacaoSimulacaoInexistenteException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro ao associar a célula a uma simulação inexistente.")

class TipoExperimentoDesconhecidoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Tipo de experimento desconhecido.")