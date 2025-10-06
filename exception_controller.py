from sistema_exceptions import SistemaException


class ExceptionController:
    def __init__(self, modo_debug: bool = False):
  

    def tratar_excecao(self, erro: Exception):
       
        if isinstance(erro, SistemaException):
            self._exibir_mensagem(f"[ERRO DO SISTEMA] {erro}")
        elif isinstance(erro, IndexError):
            self._exibir_mensagem("Tentativa de acessar índice fora do intervalo permitido.")
        elif isinstance(erro, ValueError):
            self._exibir_mensagem("Valor inválido fornecido.")
        else:
            self._exibir_mensagem(f"[ERRO DESCONHECIDO] {type(erro).__name__}: {erro}")


    def _exibir_mensagem(self, msg: str):
        print(msg)

    def executar_com_tratamento(self, funcao, *args, **kwargs):
      ##args e kwargs sao termos do python que pelo q eu vi sao uteis nesse caso args puxa como se fosse uma tupla o erro e kwargs um dicionario
        try:
            return funcao(*args, **kwargs)
        except Exception as e:
            self.tratar_excecao(e)
            return None
##pode virar tela
