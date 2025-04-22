def pilha_banco():
    pilha = []  # A pilha funciona como LIFO: o último elemento inserido é o primeiro a ser retirado.

    while True:

        print("""
        Bem Vindos ao programa de gerenciar clientes.
        ------------------------------------
        By PedCruz.
        """)

        print("\n=== Menu ===")
        # Exibindo a pilha atual (os clientes que estão na pilha).
        print("1 - Adicionar cliente [Clientes na pilha: {}]".format(", ".join(pilha) if pilha else "nenhum cliente."))
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
                pilha.append(nome)
                print(f"Cliente '{nome}' adicionado à pilha.")
            else:
                print("Nome não pode ser vazio.")
        elif opcao == 2:
            if pilha:
                cliente = pilha.pop()
                print(f"Cliente '{cliente}' foi atendido.")
            else:
                print("A pilha está vazia. Nenhum cliente para atender.")
        elif opcao == 3:
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")

# Execução do programa
pilha_banco()

# Operações em listas:
# A operação de adicionar um cliente (append()) é eficiente, com complexidade O(1). Ela adiciona um item ao final da lista (topo da pilha), sem a necessidade de deslocar outros elementos.
# A operação de remover um cliente (pop()) também é eficiente, com complexidade O(1). Ela remove o item do final da lista (topo da pilha), sem mover os elementos anteriores.
# 👌