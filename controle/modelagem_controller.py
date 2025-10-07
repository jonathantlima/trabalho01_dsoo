from limite.tela_modelagem import TelaModelagem
from entidade.modelagem import Modelagem

class ControladorModelagem:

    def __init__(self, controlador_sistema):
        self.__tela = TelaModelagem()
        self.__modelagens = []
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {
            1: self.cadastra_modelagem,
            2: self.lista_modelagens,
            0: self.retornar
        }
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida")

    def cadastra_modelagem(self):
        print("Criação de modelagem: requer simulação e condições definidas.")
        # Aqui futuramente integrará com condicao_inicial e simulacao
        print("Modelagem registrada (mock).")

    def lista_modelagens(self):
        if not self.__modelagens:
            print("Nenhuma modelagem registrada.")
        for m in self.__modelagens:
            print(m)

    def retornar(self):
        self.__controlador_sistema.abre_tela()
