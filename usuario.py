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
    