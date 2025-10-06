# limite/tela_sistema.py
class TelaSistema:
    def mostra_menu(self):
        print("\n=== SISTEMA DE SIMULAÇÃO ELETROCINÉTICA ===")
        print("1 - Gerenciar usuários")
        print("2 - Gerenciar solos")
        print("3 - Gerenciar células experimentais")
        print("4 - Definir condição inicial")
        print("5 - Modelagem")
        print("6 - Simulação")
        print("0 - Sair")
        return int(input("Escolha uma opção: "))

