# ==============================
# Exceções gerais do sistema
# ==============================
class UsuarioNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("Usuário não encontrado no sistema.")


class SimulacaoNaoEncontradaException(Exception):
    def __init__(self):
        super().__init__("Simulação inexistente ou inválida.")


class ModelagemNaoInicializadaException(Exception):
    def __init__(self):
        super().__init__("Modelagem não definida ou não inicializada.")


class CampoObrigatorioException(Exception):
    def __init__(self):
        super().__init__("Algum campo obrigatório está vazio ao criar ou editar um objeto.")


class EmailInvalidoException(Exception):
    def __init__(self):
        super().__init__("Formato de e-mail inválido.")


class UsuarioDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Usuário já cadastrado no sistema.")


class TelefoneInvalidoException(Exception):
    def __init__(self):
        super().__init__("Telefone informado possui formato inválido.")


class ParametrosFisicosInvalidosException(Exception):
    def __init__(self):
        super().__init__("Parâmetros físicos inválidos (ex.: duração negativa, solo nulo, etc.).")


class CondicaoIncompativelException(Exception):
    def __init__(self):
        super().__init__("Condições iniciais incompatíveis com o tipo de simulação.")


class EspecieQuimicaInexistenteException(Exception):
    def __init__(self):
        super().__init__("Espécie química não definida ou inexistente.")


class ErroDeUnidadeException(Exception):
    def __init__(self):
        super().__init__("Valores fora da faixa esperada (ex.: concentração negativa, etc.).")


class ErroGerarRelatorioException(Exception):
    def __init__(self):
        super().__init__("Erro ao gerar relatório de simulação.")


class TipoSoloInvalidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de solo inválido ou desconhecido.")


class ParametrosSoloInvalidosException(Exception):
    def __init__(self):
        super().__init__("Parâmetros físicos incoerentes (ex.: densidade negativa, porosidade > 1).")


class ErroCalculoPropriedadeSoloException(Exception):
    def __init__(self):
        super().__init__("Erro ao calcular propriedades derivadas do solo (ex.: divisão por zero).")


class DadosMedicaoInvalidosException(Exception):
    def __init__(self):
        super().__init__("Dados de medição ausentes ou inválidos na célula experimental.")


class SimulacaoAssociadaInexistenteException(Exception):
    def __init__(self):
        super().__init__("Erro ao associar célula experimental a uma simulação inexistente.")


class TipoExperimentoDesconhecidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de experimento desconhecido.")


class EspecieNaoDefinidaNoDominioException(Exception):
    def __init__(self):
        super().__init__("Espécie química não definida no domínio da condição.")


class ValorInicialForaDoIntervaloException(Exception):
    def __init__(self):
        super().__init__("Valores iniciais fora do intervalo físico permitido.")


class GradienteConcentracaoIndefinidoException(Exception):
    def __init__(self):
        super().__init__("Gradiente de concentração indefinido.")


class FalhaAssociacaoCondicaoModelagemException(Exception):
    def __init__(self):
        super().__init__("Falha na associação entre condição e modelagem.")


class NomeEspecieDuplicadoException(Exception):
    def __init__(self):
        super().__init__("Espécie química com nome duplicado.")


class CoeficienteDifusaoNegativoException(Exception):
    def __init__(self):
        super().__init__("Coeficiente de difusão negativo.")


class TipoDeDadoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Tipo de dado inválido (ex.: fórmula com caractere incorreto).")


class PropriedadeObrigatoriaNaoDefinidaException(Exception):
    def __init__(self):
        super().__init__("Espécie sem propriedades obrigatórias definidas.")


class ModelagemSemCondicoesException(Exception):
    def __init__(self):
        super().__init__("Modelagem sem condição inicial ou de contorno.")


class ErroCalculoNumericoException(Exception):
    def __init__(self):
        super().__init__("Erro de cálculo numérico (overflow, NaN, divisão por zero, etc.).")


class ErroPersistenciaModelagemException(Exception):
    def __init__(self):
        super().__init__("Erro ao salvar ou carregar modelo de modelagem.")


class ModelagemSemSimulacaoException(Exception):
    def __init__(self):
        super().__init__("Modelagem associada a simulação inexistente.")


class InterfaceNaoInicializadaException(Exception):
    def __init__(self):
        super().__init__("Tentativa de acessar elementos de interface não inicializados.")


class EntradaUsuarioInvalidaException(Exception):
    def __init__(self):
        super().__init__("Entrada inválida do usuário (ex.: string em campo numérico).")



