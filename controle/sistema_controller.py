from controle.usuario_controller import ControladorUsuario
from controle.condicao_inicial_controller import ControladorCondicaoInicial
from controle.modelagem_controller import ControladorModelagem
from controle.simulacao_controller import ControladorSimulacao
from controle.solo_controller import ControladorSolo
from controle.celula_experimental_controller import ControladorCelulaExperimental
from limite.tela_sistema import TelaSistema


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_solo = ControladorSolo(self)
        self.__controlador_celula = ControladorCelulaExperimental(self)
        self.__controlador_condicao_inicial = ControladorCondicaoInicial(self)
        self.__controlador_modelagem = ControladorModelagem(self)
        self.__controlador_simulacao = ControladorSimulacao(self)

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.__controlador_usuario.abre_tela,
            2: self.__controlador_solo.abre_tela,
            3: self.__controlador_celula.abre_tela,
            4: self.__controlador_condicao_inicial.abre_tela,
            5: self.__controlador_modelagem.abre_tela,
            6: self.__controlador_simulacao.abre_tela,
            0: self.encerra_sistema
        }

        while True:
            try:
                opcao = self.__tela_sistema.mostra_menu()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Por favor, digite um número válido!")
            except Exception as e:
                print(f"Erro: {e}")

    def encerra_sistema(self):
        print("\nEncerrando o sistema...")
        exit(0)

