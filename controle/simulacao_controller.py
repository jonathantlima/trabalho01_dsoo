from limite.tela_simulacao import TelaSimulacao
from entidade.simulacao import Simulacao
from datetime import date

class ControladorSimulacao:

    def __init__(self, controlador_sistema):
        self.__tela = TelaSimulacao()
        self.__simulacoes = []
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {
            1: self.cria_simulacao,
            2: self.lista_simulacoes,
            0: self.retornar
        }
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida")

    def cria_simulacao(self):
        dados = self.__tela.coleta_dados_simulacao()
        simulacao = Simulacao(data=date.today(),
                              solo=dados["solo"],
                              celula_experimental=dados["celula_experimental"],
                              modelo=dados["modelo"])
        self.__simulacoes.append(simulacao)
        print("Simulação criada!")

    def lista_simulacoes(self):
        self.__tela.mostra_simulacoes(self.__simulacoes)

    def retornar(self):
        self.__controlador_sistema.abre_tela()
