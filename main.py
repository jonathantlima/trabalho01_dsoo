from controle.sistema_controller import ControladorSistema

if __name__ == "__main__":
    try:
        ControladorSistema().inicializa_sistema()
    except Exception as e:
        print(f"Erro ao iniciar o sistema: {e}")
        import traceback
        traceback.print_exc()
