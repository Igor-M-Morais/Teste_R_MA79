#Aqui vou desenvolver o meu código de teste para a revisão.

# Array (lista) global para armazenar os dicionários de motores
motores = [
    {
        "id": 1,
        "modelo": "W22 IR3 Premium",
        "fabricante": "WEG",
        "potencia_cv": 10.0,
        "tensao_v": "220/380V",
        "rpm": 1750,
    },
    {
        "id": 2,
        "modelo": "1LE0",
        "fabricante": "Siemens",
        "potencia_cv": 5.0,
        "tensao_v": "380/660V",
        "rpm": 3500,
    },
]
proximo_id = 3


def cadastrar_motor():
    global proximo_id
    print("\n--- CADASTRAR NOVO MOTOR ---")
    modelo = input("Modelo do motor: ").strip()
    fabricante = input("Fabricante: ").strip()

    try:
        potencia = float(input("Potência (CV): "))
        rpm = int(input("Rotação (RPM): "))
    except ValueError:
        print(
            "Erro: Potência deve ser número (ex: 7.5) e RPM deve ser inteiro (ex: 1750)."
        )
        return

    tensao = input("Tensão (ex: 220/380V): ").strip()

    motor = {
        "id": proximo_id,
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia,
        "tensao_v": tensao,
        "rpm": rpm,
    }

    motores.append(motor)
    proximo_id += 1
    print(f"Sucesso: Motor '{modelo}' cadastrado com ID {motor['id']}!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(
            f"ID: {m['id']} | Modelo: {m['modelo']} | Fab: {m['fabricante']} | "
            f"Potência: {m['potencia_cv']} CV | Tensão: {m['tensao_v']} | RPM: {m['rpm']}"
        )


def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    termo = input("Digite o ID ou parte do nome do modelo/fabricante: ").strip().lower()
    encontrados = []

    for m in motores:
        if (
            termo == str(m["id"])
            or termo in m["modelo"].lower()
            or termo in m["fabricante"].lower()
        ):
            encontrados.append(m)

    if not encontrados:
        print("Nenhum motor encontrado com esse critério.")
    else:
        for m in encontrados:
            print(
                f"ID: {m['id']} | Modelo: {m['modelo']} | Fab: {m['fabricante']} | "
                f"Potência: {m['potencia_cv']} CV | Tensão: {m['tensao_v']} | RPM: {m['rpm']}"
            )


def atualizar_motor():
    print("\n--- ATUALIZAR MOTOR ---")
    try:
        id_busca = int(input("Digite o ID do motor que deseja alterar: "))
    except ValueError:
        print("ID inválido.")
        return

    for m in motores:
        if m["id"] == id_busca:
            print(f"Editando: {m['modelo']} (Deixe em branco para manter o atual)")

            novo_modelo = input(f"Novo modelo [{m['modelo']}]: ").strip()
            novo_fab = input(f"Novo fabricante [{m['fabricante']}]: ").strip()
            nova_pot = input(f"Nova potência CV [{m['potencia_cv']}]: ").strip()
            nova_tensao = input(f"Nova tensão [{m['tensao_v']}]: ").strip()
            novo_rpm = input(f"Novo RPM [{m['rpm']}]: ").strip()

            if novo_modelo:
                m["modelo"] = novo_modelo
            if novo_fab:
                m["fabricante"] = novo_fab
            if nova_pot:
                try:
                    m["potencia_cv"] = float(nova_pot)
                except ValueError:
                    print("Potência inválida, valor anterior mantido.")
            if nova_tensao:
                m["tensao_v"] = nova_tensao
            if novo_rpm:
                try:
                    m["rpm"] = int(novo_rpm)
                except ValueError:
                    print("RPM inválido, valor anterior mantido.")

            print("Motor atualizado com sucesso!")
            return

    print("Motor não encontrado.")


def excluir_motor():
    print("\n--- EXCLUIR MOTOR ---")
    try:
        id_busca = int(input("Digite o ID do motor que deseja excluir: "))
    except ValueError:
        print("ID inválido.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_busca:
            removido = motores.pop(i)
            print(
                f"Motor '{removido['modelo']}' (ID {removido['id']}) removido com sucesso!"
            )
            return

    print("Motor não encontrado.")


def menu():
    while True:
        print("\n==============================")
        print("  SISTEMA DE CADASTRO DE MOTORES")
        print("==============================")
        print("1. Cadastrar Motor")
        print("2. Listar Todos")
        print("3. Buscar Motor")
        print("4. Atualizar Motor")
        print("5. Excluir Motor")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            excluir_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu()