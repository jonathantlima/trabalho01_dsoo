from entidade.usuario import Usuario
from limite.tela_usuario import TelaUsuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def abre_tela(self):
        opcoes = {
            1: self.cadastrar_usuario,
            2: self.listar_usuarios,
            3: self.alterar_usuario,
            0: self.retornar
        }
        while True:
            try:
                opcao = self.__tela_usuario.mostra_menu()
                if opcao in opcoes:
                    opcoes[opcao]()
                else:
                    print("Opção inválida")
            except ValueError:
                print("Por favor, digite um número válido!")
            except Exception as e:
                print(f"Erro: {e}")

    def cadastrar_usuario(self):
        try:
            usuario_dict = self.__tela_usuario.coleta_dados_usuario()
            usuario = Usuario(usuario_dict["nome"], usuario_dict["email"], usuario_dict["telefone"], usuario_dict["departamento"], usuario_dict["matricula"])
            self.__usuarios.append(usuario)
            self.__tela_usuario.imprime_mensagem(f"Usuário cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def listar_usuarios(self):
        for usuario in self.__usuarios:
            dados_usuario = {"nome": usuario.nome, "email": usuario.email, "telefone": usuario.telefone, "departamento": usuario.departamento, "matricula": usuario.matricula}
            self.__tela_usuario.mostra_usuario(dados_usuario)

    def alterar_usuario(self):
        try:
            matricula = input("Digite a matrícula do usuário a alterar: ")
            for usuario in self.__usuarios:
                if usuario.matricula == matricula:
                    novos_dados = self.__tela_usuario.coleta_dados_usuario()
                    usuario.nome = novos_dados["nome"]
                    usuario.email = novos_dados["email"]
                    usuario.telefone = novos_dados["telefone"]
                    usuario.departameno = novos_dados["departamento"]
                    print("Dados atualizados.")
                    return
            print("Usuário não encontrado.")
        except Exception as e:
            print(f"Erro ao alterar usuário: {e}")

    def retornar(self):
        self.__controlador_sistema.abre_tela()
