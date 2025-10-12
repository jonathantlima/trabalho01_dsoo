from entidade.cation import Cation
from entidade.anion import Anion
from entidade.condicao_inicial import CondicaoInicial
from limite.tela_condicao_inicial import TelaCondicaoInicial


class ControladorCondicaoInicial:
    def __init__(self, controlador_sistema):
        self.__tela = TelaCondicaoInicial()
        self.__condicao_inicial = None
        self.__controlador_sistema = controlador_sistema  # referência ao sistema principal

    def abre_tela(self):
        opcoes = {
            1: self.set_condicao_inicial,
            2: self.get_condicao_inicial,
            3: self.mostra_condicao_inicial,
            0: self.retornar
        }
        while True:
            opcao = self.__tela.tela_opcoes()
            if opcao in opcoes:
                opcoes[opcao]()
            else:
                self.__tela.imprime_mensagem("Opção inválida")

    def set_condicao_inicial(self):
        try:
            concentracao_inicial = self.__tela.coleta_dados_concentracao_inicial()
            nome, formula, funcao, valencia, coeficiente_de_difusao = self.__tela.coleta_dados_especie_quimica()

            while True:
                ion = input("Escolha o tipo de íon:\n1 - Cátion\n2 - Ânion\n> ")
                if ion == "1":
                    especie_quimica = Cation(nome, formula, funcao, valencia, coeficiente_de_difusao)
                    self.__tela.imprime_mensagem("Cátion criado com sucesso.")
                    break
                elif ion == "2":
                    especie_quimica = Anion(nome, formula, funcao, valencia, coeficiente_de_difusao)
                    self.__tela.imprime_mensagem("Ânion criado com sucesso.")
                    break
                else:
                    self.__tela.imprime_mensagem("Tipo inválido. Retornando ao menu.")
                    return

            gradiente_eletrico = self.__tela.coleta_gradiente_eletrico()
            gradiente_hidraulico = self.__tela.coleta_gradiente_hidraulico()

            self.__condicao_inicial = CondicaoInicial(
                gradiente_eletrico,
                gradiente_hidraulico,
                especie_quimica,
                concentracao_inicial
            )
            self.__tela.imprime_mensagem("Condição inicial configurada com sucesso!")
            return self.__condicao_inicial
        except Exception as e:
            self.__tela.imprime_mensagem(f"Erro ao configurar a condição inicial: {e}")

    def mostra_condicao_inicial(self):
        if self.__condicao_inicial:
            self.__tela.exibe_condicao_inicial(self.__condicao_inicial)
        else:
            self.__tela.imprime_mensagem("Nenhuma condição inicial cadastrada ainda.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def get_condicao_inicial(self):
        return self.__condicao_inicial
