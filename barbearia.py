# barbearia.py

# Lista de serviços e preços
SERVICOS = {
    "1": ("Americano", 40.0),
    "2": ("Mid Fade", 40.0),
    "3": ("Moicano", 40.0),
    "4": ("Social", 30.0),
    "5": ("Mullet", 40.0),
    "6": ("Low Fade", 35.0),
    "7": ("Sobrancelha e Bigode", 10.0),
    "8": ("Luzes", 150.0),
    "9": ("Pigmentação", 100.0),
    "10": ("Alisamento", 85.0)
}

# Lista para armazenar os agendamentos na memória
agendamentos = []

def exibir_menu_servicos():
    print("\n--- SERVIÇOS E PREÇOS ---")
    for chave, (nome, preco) in SERVICOS.items():
        print(f"[{chave}] {nome} - R$ {preco:.2f}")

def agendar_cliente():
    print("\n--- AGENDAR CLIENTE ---")
    nome_cliente = input("Nome do cliente: ").strip()
    if not nome_cliente:
        print("Nome não pode ser vazio.")
        return

    horario = input("Horário (ex: 14:00): ").strip()
    
    exibir_menu_servicos()
    opcao = input("Escolha o número do serviço: ").strip()

    if opcao in SERVICOS:
        servico_nome, preco = SERVICOS[opcao]
        agendamento = {
            "cliente": nome_cliente,
            "horario": horario,
            "servico": servico_nome,
            "preco": preco
        }
        agendamentos.append(agendamento)
        print(f"\n✅ Agendamento realizado com sucesso para {nome_cliente}!")
    else:
        print("\n❌ Opção de serviço inválida. Agendamento cancelado.")

def listar_agendamentos():
    print("\n--- CLIENTES AGENDADOS ---")
    if not agendamentos:
        print("Nenhum cliente agendado até o momento.")
        return

    total_faturado = 0.0
    for idx, ag in enumerate(agendamentos, 1):
        print(f"{idx}. Cliente: {ag['cliente']} | Horário: {ag['horario']} | Serviço: {ag['servico']} | Valor: R$ {ag['preco']:.2f}")
        total_faturado += ag['preco']
    
    print("-" * 40)
    print(f"Total previsto: R$ {total_faturado:.2f}")

def main():
    while True:
        print("\n=== SISTEMA DE BARBEARIA ===")
        print("1. Ver Serviços e Preços")
        print("2. Agendar Cliente")
        print("3. Ver Clientes Agendados")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_menu_servicos()
        elif opcao == "2":
            agendar_cliente()
        elif opcao == "3":
            listar_agendamentos()
        elif opcao == "4":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida, tente novamente.")

if __name__ == "__main__":
    main()