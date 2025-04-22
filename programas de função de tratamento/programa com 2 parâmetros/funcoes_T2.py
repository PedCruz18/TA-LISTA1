def pega_inteiro(mensagem: str, mensagem_erro: str, menor_valor: int = None, maior_valor: int = None) -> int:
    while True:
        try:
            valor = int(input(mensagem))

            if (menor_valor is not None and valor < menor_valor):
                print(f"Valor deve ser maior ou igual a {menor_valor}.")
                continue

            if (maior_valor is not None and valor > maior_valor):
                print(f"Valor deve ser menor ou igual a {maior_valor}.")
                continue

            return valor

        except ValueError:
            print(mensagem_erro)