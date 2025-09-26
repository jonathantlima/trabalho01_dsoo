class Usuario:
    
    def __init__(self, nome: str, email: str, telefone: str, curso: str, matricula: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str):
            self.__email = email
        if isinstance(telefone, str):
            self.__telefone = telefone
        if isinstance(curso, str):
            self.__curso = curso
        if isinstance(matricula, str):
            self.__matricula = matricula
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, email: str):
        if isinstance(email, str):
            self.__email = email
    
    @property
    def telefone(self) -> str:
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone: str):
        if isinstance(telefone, str):
            self.__telefone = telefone
    
    @property
    def curso(self) -> str:
        return self.__curso
    
    @curso.setter
    def curso(self, curso: str):
        if isinstance(curso, str):
            self.__curso = curso

    def cadastrar(self, nome: str, email: str, telefone: str, curso: str, matricula: str):
        """Cadastra ou atualiza os dados do usuário"""
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.curso = curso
        self.matricula = matricula
    
    def consultar(self) -> None:
        """Exibe os dados do usuário em forma de print"""
        print(f"--- Dados do Usuário ---")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Curso: {self.curso}")
        print(f"Matrícula: {self.matricula}")

    
