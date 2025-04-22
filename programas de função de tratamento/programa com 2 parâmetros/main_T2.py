from funcoes_T2 import pega_inteiro

def main():
    print()
    numero = pega_inteiro(
        mensagem="Informe um número entre 10 e 100: ",
        mensagem_erro="Entrada inválida. Digite um número inteiro!",
        menor_valor=10,
        maior_valor=100
    )
    print(f"Número aceito: {numero}")
    print()

if __name__ == "__main__":
    main()
