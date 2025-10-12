from .erro_sistema_exception import ErroSistemaException

class ElementoInterfaceNaoInicializadoException(ErroSistemaException):
    def __init__(self):
        super().__init__("Acesso a elementos de interface não inicializados.")

class EntradaUsuarioInvalidaException(ErroSistemaException):
    def __init__(self):
        super().__init__("Entrada do usuário inválida (ex.: string em campo numérico).")