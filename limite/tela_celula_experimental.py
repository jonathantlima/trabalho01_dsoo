class TelaCelulaExperimental:
    def mostra_menu(self):
        print("=== MENU CÉLULA EXPERIMENTAL ===")
        print("1 - Cadastrar célula")
        print("2 - Listar células")
        print("0 - Voltar")
        return int(input("Escolha: "))

    def coleta_dados_celula(self):
        material = input("Material da célula: ")
        comprimento = float(input("Comprimento (m): "))
        diametro = float(input("Diâmetro (m): "))
        return {"material": material, "comprimento": comprimento, "diametro": diametro}

    def mostra_celulas(self, celulas):
        if not celulas:
            print("Nenhuma célula cadastrada.")
            return
        for c in celulas:
            print(f"{c.material} - {c.comprimento}m x {c.diametro}m")
