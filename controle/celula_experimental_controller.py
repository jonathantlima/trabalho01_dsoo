from entidade.celula_experimental import CelulaExperimental
from limite.tela_celula_experimental import TelaCelulaExperimental

class ControladorCelulaExperimental:

    def __init__(self, controlador_sistema):
        self.__celulas = []
        self.__tela = TelaCelulaExperimental()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {
            1: self.cadastra_celula,
            2: self.lista_celulas,
            0: self.retornar
        }
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida")

    def cadastra_celula(self):
        dados = self.__tela.coleta_dados_celula()
        celula = CelulaExperimental(**dados)
        self.__celulas.append(celula)
        print("Célula experimental cadastrada!")

    def lista_celulas(self):
        self.__tela.mostra_celulas(self.__celulas)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def get_celulas(self):
        return self.__celulas
