class TelaSolo:
    def mostra_menu(self):
        print("=== MENU SOLO ===")
        print("1 - Cadastrar solo")
        print("2 - Listar solos")
        print("3 - Alterar solo")
        print("0 - Voltar")
        return int(input("Escolha: "))

    def coleta_dados_solo(self):
        tipo = input("Tipo (areia, argila, silte): ")
        origem = input("Origem: ")
        cor = input("Cor: ")
        porosidade = float(input("Porosidade: "))
        massa_especifica_seca = float(input("Massa específica seca: "))
        condutividade_hidraulica = float(input("Condutividade hidráulica: "))
        permeabilidade_eletroosmotica = float(input("Permeabilidade eletrosmótica: "))
        return {
            "tipo": tipo, "origem": origem, "cor": cor,
            "porosidade": porosidade,
            "massa_especifica_seca": massa_especifica_seca,
            "condutividade_hidraulica": condutividade_hidraulica,
            "permeabilidade_eletroosmotica": permeabilidade_eletroosmotica
        }

    def mostra_solos(self, solos):
        if not solos:
            print("Nenhum solo cadastrado.")
            return
        for s in solos:
            print(f"{s.tipo} ({s.cor}) - origem: {s.origem}")
