# usuario.py
class Usuario:
    def __init__(self, nome: str, email: str, telefone: str, curso: str, matricula: str):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__curso = curso
        self.__matricula = matricula

    # Getters e Setters
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, novo_email: str):
        self.__email = novo_email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone: str):
        self.__telefone = novo_telefone

    @property
    def curso(self) -> str:
        return self.__curso

    @curso.setter
    def curso(self, novo_curso: str):
        self.__curso = novo_curso

    @property
    def matricula(self) -> str:
        return self.__matricula

    @matricula.setter
    def matricula(self, nova_matricula: str):
        self.__matricula = nova_matricula

    def __str__(self):
        return (f"Nome: {self.__nome}\n"
                f"Email: {self.__email}\n"
                f"Telefone: {self.__telefone}\n"
                f"Curso: {self.__curso}\n"
                f"Matrícula: {self.__matricula}")
