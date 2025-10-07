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
        curso = input("Curso: ")
        matricula = input("Matrícula: ")
        return {"nome": nome, "email": email, "telefone": telefone, "curso": curso, "matricula": matricula}
    ##viola o mvc
    def mostra_usuario(self, usuario):
        print(" >>> DADOS DO USUÁRIO <<<")
        print("----- Nome ----- email ----- curso ----- matricula -----")
        print(f"{usuario.nome} - {usuario.email} - {usuario.curso} ({usuario.matricula})")
