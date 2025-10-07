class TipoErradoException(Exception):
    def __init__(self):
        super().__init__("Entrada de dado com tipo errado.")