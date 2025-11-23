import FreeSimpleGUI as sg

class TelaUsuario:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # ================= MENU USUÁRIO ==================
    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()

        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3

        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('-------- USUÁRIOS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção', font=("Helvica", 15))],

            [sg.Radio('Cadastrar Usuário', "RD1", key='1')],
            [sg.Radio('Alterar Usuário', "RD1", key='2')],
            [sg.Radio('Listar Usuários', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Menu Usuários').Layout(layout)

    # ================= DADOS DO USUÁRIO ==================
    def coleta_dados(self, dados_iniciais=None):
        sg.ChangeLookAndFeel('DarkTeal4')
        dados_iniciais = dados_iniciais or {}

        layout = [
            [sg.Text('-------- CADASTRO DE USUÁRIO ----------', font=("Helvica", 25))],

            [sg.Text('Nome:', size=(20, 1)), sg.InputText(dados_iniciais.get('nome', ''), key='nome')],
            [sg.Text('Email:', size=(20, 1)), sg.InputText(dados_iniciais.get('email', ''), key='email')],
            [sg.Text('Telefone:', size=(20, 1)), sg.InputText(dados_iniciais.get('telefone', ''), key='telefone')],
            [sg.Text('Departamento:', size=(20, 1)), sg.InputText(dados_iniciais.get('departamento', ''), key='departamento')],
            [sg.Text('Matrícula:', size=(20, 1)), sg.InputText(dados_iniciais.get('matricula', ''), key='matricula')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Cadastro Usuário').Layout(layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        return values

    # ================= MATRÍCULA ==================
    def coleta_matricula_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('-------- BUSCAR USUÁRIO ----------', font=("Helvica", 25))],
            [sg.Text('Digite a matrícula:', font=("Helvica", 15))],
            [sg.InputText('', key='matricula')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Busca Usuário').Layout(layout)
        button, values = self.open()

        matricula = values['matricula'] if button == 'Confirmar' else None
        self.close()
        return matricula

    def mostra_mensagem(self, msg):
        sg.Popup("", msg)

    def open(self):
        return self.__window.Read()

    def close(self):
        self.__window.Close()
