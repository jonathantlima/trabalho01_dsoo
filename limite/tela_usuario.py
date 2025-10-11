# tela_usuario.py
class TelaUsuario:
    def mostra_menu(self):
        print("=== MENU USUÁRIO ===")
        print("1 - Cadastrar novo usuário")
        print("2 - Listar usuários")
        print("3 - Alterar dados")
        print("0 - Voltar")
        return int(input("Escolha: "))

    def coleta_dados_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        departamento = input("Departamento: ")
        matricula = input("Matrícula: ")
        return {"nome": nome, "email": email, "telefone": telefone, "departamento": departamento, "matricula": matricula}

    def mostra_usuario(self, dados_usuario):
        print(" >>> DADOS DO USUÁRIO <<<")
        print("----- Nome ----- Email ----- Departamento -----( Matricula )-----")
        print(f"{dados_usuario["nome"]} - {dados_usuario["email"]} - {dados_usuario["departamento"]} ({dados_usuario["matricula"]})")
    
    def imprime_mensagem(self, mensagem: str):
        if isinstance(mensagem, str):
            print(mensagem)
