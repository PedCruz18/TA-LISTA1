def entrada_inteiro(mensagem: str, mensagem_erro: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))  # Tentativa de converter para inteiro
            return valor  # Retorna o número inteiro válido
        except ValueError:
            print(mensagem_erro)  # Caso ocorra um erro, exibe a mensagem de erro