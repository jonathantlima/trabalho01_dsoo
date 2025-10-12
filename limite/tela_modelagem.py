class TelaModelagem:
    def mostra_menu(self):
        print("=== MENU MODELAGEM ===")
        print("1 - Criar modelagem")
        print("2 - Alterar modelagem")
        print("3 - Listar modelagens")
        print("0 - Voltar")
        return int(input("Escolha: "))
    
    def imprime_mensagem(self, mensagem):
        print(mensagem)
    
    def coleta_dados(self):
        print(">>>>> COLETA DE DADOS DA MODELAGEM <<<<<")
