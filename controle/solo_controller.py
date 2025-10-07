from entidade.areia import Areia
from entidade.argila import Argila
from entidade.silte import Silte
from limite.tela_solo import TelaSolo

class ControladorSolo:

    def __init__(self, controlador_sistema):
        self.__solos = []
        self.__tela = TelaSolo()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {
            1: self.cadastra_solo,
            2: self.lista_solos,
            3: self.altera_solo,
            0: self.retornar
        }
        while True:
            opcao = self.__tela.mostra_menu()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                print("Opção inválida")

    def cadastra_solo(self):
        dados = self.__tela.coleta_dados_solo()
        tipo = dados["tipo"].lower()
        if tipo == "areia":
            solo = Areia(**dados)
        elif tipo == "argila":
            solo = Argila(**dados)
        elif tipo == "silte":
            solo = Silte(**dados)
        else:
            print("Tipo de solo não reconhecido.")
            return
        self.__solos.append(solo)
        print("Solo cadastrado com sucesso!")

    def lista_solos(self):
        self.__tela.mostra_solos(self.__solos)

    def altera_solo(self):
        nome = input("Digite o tipo do solo a alterar: ")
        for s in self.__solos:
            if s.tipo == nome:
                novos_dados = self.__tela.coleta_dados_solo()
                s.tipo = novos_dados["tipo"]
                s.origem = novos_dados["origem"]
                s.cor = novos_dados["cor"]
                s.porosidade = novos_dados["porosidade"]
                s.massa_especifica_seca = novos_dados["massa_especifica_seca"]
                s.condutividade_hidraulica = novos_dados["condutividade_hidraulica"]
                s.permeabilidade_eletroosmotica = novos_dados["permeabilidade_eletroosmotica"]
                print("Dados atualizados!")
                return
        print("Solo não encontrado.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def get_solos(self):
        return self.__solos
