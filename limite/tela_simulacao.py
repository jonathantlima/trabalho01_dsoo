class TelaSimulacao:
    def mostra_menu(self):
        print("=== MENU SIMULAÇÃO ===")
        print("1 - Criar simulação")
        print("2 - Listar simulações")
        print("0 - Voltar")
        return int(input("Escolha: "))

    def coleta_dados_simulacao(self):
        print("Simulação: mock simples (associações automáticas futuramente).")
        # placeholders, futuramente integrará com controladores
        return {"solo": None, "celula_experimental": None, "modelo": None}

    def mostra_simulacoes(self, simulacoes):
        if not simulacoes:
            print("Nenhuma simulação cadastrada.")
            return
        for s in simulacoes:
            print(f"Simulação em {s.data}")
