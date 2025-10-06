from entidade.cation import Cation
from entidade.anion import Anion
from entidade.condicao_inicial import CondicaoInicial
from limite.tela_condicao_inicial import TelaCondicaoInicial


class ControladorCondicaoInicial:
    def __init__(self, controlador_sistema):
        self.__view = TelaCondicaoInicial()
        self.__condicao_inicial = None
        self.__controlador_sistema = controlador_sistema  # referência ao sistema principal

    def apresenta_menu(self):
        opcoes = {
            1: self.set_condicao_inicial,
            2: self.set_condicao_inicial,
            3: self.mostra_condicao_inicial,
            0: self.retornar
        }

        while True:
            try:
                opcao = self.__view.tela_opcoes()
                funcao = opcoes.get(opcao)
                if funcao:
                    funcao()
                else:
                    print("Opção inválida!")
            except ValueError:
                print("Número inválido!")

    def set_condicao_inicial(self):
        try:
            concentracao_inicial = self.__view.coleta_dados_concentracao_inicial()
            nome, formula, funcao, valencia, coeficiente_de_difusao = self.__view.coleta_dados_especie_quimica()

            while True:
                ion = input("Escolha o tipo de íon:\n1 - Cátion\n2 - Ânion\n> ")
                if ion == "1":
                    especie_quimica = Cation(nome, formula, funcao, valencia, coeficiente_de_difusao)
                elif ion == "2":
                    especie_quimica = Anion(nome, formula, funcao, valencia, coeficiente_de_difusao)
                else:
                    print("Tipo inválido. Retornando ao menu.")
                    return

            gradiente_eletrico = self.__view.coleta_gradiente_eletrico()
            gradiente_hidraulico = self.__view.coleta_gradiente_hidraulico()

            self.__condicao_inicial = CondicaoInicial(
                gradiente_eletrico,
                gradiente_hidraulico,
                especie_quimica,
                concentracao_inicial
            )
            print("Condição inicial configurada com sucesso!")
            return self.__condicao_inicial
        except Exception as e:
            print(f"Erro ao configurar a condição inicial: {e}")

    def mostra_condicao_inicial(self):
        if self.__condicao_inicial:
            self.__view.exibe_condicao_inicial(self.__condicao_inicial)
        else:
            print("Nenhuma condição inicial cadastrada ainda.")

    def retornar(self):
        # Apenas volta ao menu principal sem novo import
        return
    
    def get_condicao_inicial(self):
        return self.__condicao_inicial

        