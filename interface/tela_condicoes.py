import FreeSimpleGUI as sg

class TelaCondicoes:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # ================= MENU CONDIÇÕES ==================
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
            [sg.Text('------ CONDIÇÕES DO PROBLEMA ------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção', font=("Helvica", 15))],

            [sg.Radio('Cadastrar Condições', "RD1", key='1')],
            [sg.Radio('Buscar Condições', "RD1", key='2')],
            [sg.Radio('Listar Condições', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Menu Condições').Layout(layout)

    # ================= CADASTRO CONDIÇÕES ==================
    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('------ CADASTRO DE CONDIÇÕES ------', font=("Helvica", 25))],

            [sg.Text('Código:', size=(25, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Concentração Inicial (mg/L):', size=(25, 1)), sg.InputText('', key='cin')],
            [sg.Text('Gradiente Elétrico (V/cm):', size=(25, 1)), sg.InputText('', key='ge')],
            [sg.Text('Gradiente Hidráulico (cm/cm):', size=(25, 1)), sg.InputText('', key='gh')],
            [sg.Text('Concentração Reservatório (mg/L):', size=(25, 1)), sg.InputText('', key='cres')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Cadastro Condições').Layout(layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            values['cin'] = float(values['cin'])
            values['ge'] = float(values['ge'])
            values['gh'] = float(values['gh'])
            values['cres'] = float(values['cres'])
        except:
            sg.Popup("Erro: valores numéricos inválidos.")
            self.close()
            return None

        self.close()
        return values

    # ================= CÓDIGO CONDIÇÕES ==================
    def coleta_codigo_condicoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('------ BUSCAR CONDIÇÕES ------', font=("Helvica", 25))],
            [sg.Text('Digite o código:', font=("Helvica", 15))],
            [sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Busca Condições').Layout(layout)
        button, values = self.open()

        codigo = values['codigo'] if button == 'Confirmar' else None
        self.close()
        return codigo

    def mostra_mensagem(self, msg):
        sg.Popup("", msg)

    def open(self):
        return self.__window.Read()

    def close(self):
        self.__window.Close()
