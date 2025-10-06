class CondicaoDeContorno:

    def __init__(self, concentracao_reservatorio: float):
        if isinstance(concentracao_reservatorio, float):
            self.__concentracao_reservatorio = concentracao_reservatorio
        
    @property
    def concentracao_reservatorio(self) -> float:
        return self.__concentracao_reservatorio
    
    @concentracao_reservatorio.setter
    def concentracao_reservatorio(self, concentracao: float):
        if isinstance(concentracao, float):
            self.__concentracao_reservatorio = concentracao