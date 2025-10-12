from .erro_sistema_exception import ErroSistemaException

class UsuarioNaoEncontradoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Usuário não encontrado.")

class SimulacaoNaoEncontradaException(ErroSistemaException):
    def __init__(self):
        super().__init__("Simulação inexistente ou inválida.")

class ModelagemNaoInicializadaException(ErroSistemaException):
    def __init__(self):
        super().__init__("Modelagem não foi inicializada.")

class CampoObrigatorioException(ErroSistemaException):
    def __init__(self, campo=""):
        msg = f"Campo obrigatório vazio: {campo}" if campo else "Campo obrigatório vazio."
        super().__init__(msg)