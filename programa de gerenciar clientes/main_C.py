def fila_banco():
    fila = []  # Usando uma lista comum/fila FIFO

    while True:

        print("""
        Bem Vindos ao programa de gerenciar clientes.
        ------------------------------------
        By PedCruz.
        """)

        print("\n=== Menu ===")
        # Exibe a lista de clientes na fila
        print("1 - Adicionar cliente [Clientes na fila: {}]".format(", ".join(fila) if fila else "nenhum cliente."))
        print("2 - Atender cliente")
        print("3 - Fim")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if opcao == 1:
            nome = input("Digite o nome do cliente: ").strip()
            if nome:
                fila.append(nome)  # Adiciona o cliente no final da lista (fim da fila)
                print(f"Cliente '{nome}' adicionado à fila.")
            else:
                print("Nome não pode ser vazio.")
        elif opcao == 2:
            if fila:
                cliente = fila.pop(0)  # Remove o primeiro cliente da lista (início da fila)
                print(f"Cliente '{cliente}' foi atendido.")
            else:
                print("A fila está vazia. Nenhum cliente para atender.")
        elif opcao == 3:
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

# Execução do programa
fila_banco()

# umas considerações de Performance:
# append(): A operação de adicionar um cliente ao final da lista é eficiente (complexidade O(1)).
# pop(0): porém, a operação pop(0) não é eficiente para listas grandes, pois exige mover todos os elementos subsequentes para a esquerda, o que tem complexidade O(n).
# uma solução para isso é usar collections.deque, que é uma fila eficiente em Python.
# 😎