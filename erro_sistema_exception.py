class ErroSistemaException(Exception):
    """Exceção base para todo o sistema."""
    def __init__(self, mensagem="Erro no sistema."):
        super().__init__(mensagem)