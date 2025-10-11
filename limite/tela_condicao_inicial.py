class TelaCondicaoInicial:

    def tela_opcoes(self):
        print(">>> CONDIÇÃO INICIAL <<<")
        print("Selecione uma opção")
        print("1 - Configurar condição inicial")
        print("2 - Receber condicao inicial")
        print("3 - Exibir condição inicial")
        print("0 - Retornar")

        opcao = int(input("Digite sua opção: "))
        return opcao

    def coleta_dados_especie_quimica(self):
        nome = input("Digite o nome do composto: ")
        formula = input("Digite a fórmula do composto: ")
        funcao = input("Digite a função química do composto: ")
        valencia = int(input("Digite o valor da valência iônica: "))
        coeficiente_de_difusao = float(input("Digite o valor do coeficiente de difusão: "))

        return nome, formula, funcao, valencia, coeficiente_de_difusao
    
    def coleta_dados_concentracao_inicial(self):
        concentracao_esquerda = float(input("Entre com o valor da concentração no lado esquerdo da célula: "))
        concentracao_direita = float(input("Entre com o valor da concentração no lado direito da célula: "))
        return [concentracao_esquerda,concentracao_direita]
    
    def coleta_gradiente_eletrico(self):
        gradiente_eletrico = float(input("Digite o valor do gradiente elétrico: "))
        return gradiente_eletrico
    
    def coleta_gradiente_hidraulico(self):
        gradiente_hidraulico = float(input("Digite o valor do gradiente hidráulico: "))
        return gradiente_hidraulico
    
    def verifica_tipo_ionico(self):
        check = '''
                    1. cátion (carga positiva)
                    2. ânion (carga negativa)
                '''
        return check
    
    def exibe_condicao_inicial(self, condicao_inicial):
        print(">>>>>> CONDIÇÃO INICIAL <<<<<<")
        print("------------------------------")
        print("---Gradientes de Potenciais---")
        print("Gradiente elétrico: ",condicao_inicial.gradiente_eletrico)
        print("Gradiente hidráulico: ", condicao_inicial.gradiente_hidraulico)
        print("-------Espécie Química--------")
        print("Nome do composto: ", condicao_inicial.especie_quimica.nome)
        print("Fórmula química: ", condicao_inicial.especie_quimica.formula)
        print("Função química: ", condicao_inicial.especie_quimica.funcao)
        print("Coeficiente de difusao: ", condicao_inicial.especie_quimica.coeficiente_de_difusao)
