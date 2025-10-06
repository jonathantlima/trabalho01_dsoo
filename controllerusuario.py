# usuario_controller.py
from usuario import Usuario
class UsuarioController:
    def __init__(self, view=None):
        self.__usuarios = []
        self.__view = view  # TelaUsuario (opcional)

    # Exibe menu básico
    def menu(self):
        print("=== MENU USUÁRIO ===")
        print("1 - Cadastrar usuário")
        print("2 - Modificar cadastro")
        print("3 - Listar usuários")
        print("4 - Gerar relatório")
        print("0 - Voltar")

    # Cadastro de novo usuário
    def cadastra_usuario(self, nome, email, telefone, curso, matricula):
        usuario = Usuario(nome, email, telefone, curso, matricula)
        self.__usuarios.append(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso!")

    # Modifica dados de um usuário existente
    def modifica_cadastro(self, matricula, **novos_dados):
        for usuario in self.__usuarios:
            if usuario.matricula == matricula:
                if "nome" in novos_dados:
                    usuario.nome = novos_dados["nome"]
                if "email" in novos_dados:
                    usuario.email = novos_dados["email"]
                if "telefone" in novos_dados:
                    usuario.telefone = novos_dados["telefone"]
                if "curso" in novos_dados:
                    usuario.curso = novos_dados["curso"]
                print(f"Cadastro do usuário '{matricula}' atualizado.")
                return
        print("Usuário não encontrado.")

    # Lista todos os usuários cadastrados
    def lista_usuarios(self):
        if not self.__usuarios:
            print("Nenhum usuário cadastrado.")
        for u in self.__usuarios:
            print("--------------------")
            print(u)

    # Gera relatório simples dos usuários
    def gera_relatorio(self):
        print("=== RELATÓRIO DE USUÁRIOS ===")
        for u in self.__usuarios:
            print(f"{u.nome} - {u.curso} ({u.matricula})")
        print(f"Total de usuários: {len(self.__usuarios)}")

    # Getter opcional para acessar lista
    @property
    def usuarios(self):
        return self.__usuarios
