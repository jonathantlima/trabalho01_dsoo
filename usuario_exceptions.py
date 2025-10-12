from .erro_sistema_exception import ErroSistemaException

class EmailInvalidoException(ErroSistemaException):
    def __init__(self, email=""):
        super().__init__(f"Email inválido: {email}")

class UsuarioDuplicadoException(ErroSistemaException):
    def __init__(self, email=""):
        super().__init__(f"Usuário já cadastrado: {email}")

class TelefoneInvalidoException(ErroSistemaException):
    def __init__(self, telefone=""):
        super().__init__(f"Telefone inválido: {telefone}")