from .erro_sistema_exception import ErroSistemaException

class ErroConexaoBancoDadosException(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro de conexão com o banco de dados.")

class TelaError(ErroSistemaException):
    def __init__(self):
        super().__init__("Erro genérico na interface do sistema.")