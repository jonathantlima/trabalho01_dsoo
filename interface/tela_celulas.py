import FreeSimpleGUI as sg

class TelaCelulas:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    # ================= MENU CÉLULAS ==================
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
            [sg.Text('-------- CÉLULAS EXPERIMENTAIS ----------', font=("Helvica", 25))],
            [sg.Text('Escolha uma opção', font=("Helvica", 15))],

            [sg.Radio('Cadastrar Célula', "RD1", key='1')],
            [sg.Radio('Buscar Célula', "RD1", key='2')],
            [sg.Radio('Listar Células', "RD1", key='3')],
            [sg.Radio('Retornar', "RD1", key='0')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Menu Células').Layout(layout)

    # ================= CADASTRO CÉLULA ==================
    def coleta_dados(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('-------- CADASTRO DE CÉLULA ----------', font=("Helvica", 25))],

            [sg.Text('Código:', size=(20, 1)), sg.InputText('', key='codigo')],
            [sg.Text('Material:', size=(20, 1)), sg.InputText('', key='material')],
            [sg.Text('Comprimento (cm):', size=(20, 1)), sg.InputText('', key='comprimento')],
            [sg.Text('Diâmetro (cm):', size=(20, 1)), sg.InputText('', key='diametro')],

            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Cadastro Célula').Layout(layout)
        button, values = self.open()

        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            values['comprimento'] = float(values['comprimento'])
            values['diametro'] = float(values['diametro'])
        except:
            sg.Popup("Erro: valores numéricos inválidos.")
            self.close()
            return None

        self.close()
        return values

    # ================= CÓDIGO CÉLULA ==================
    def coleta_codigo_celula(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('-------- BUSCAR CÉLULA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código:', font=("Helvica", 15))],
            [sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')],
        ]

        self.__window = sg.Window('Busca Célula').Layout(layout)
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
