from funcoes_T import entrada_inteiro

def main():
    print()
    numero = entrada_inteiro(
        mensagem="Por favor, informe um número inteiro: ",
        mensagem_erro="Valor inválido. Por favor, informe um número inteiro válido!"
    )
    print(f"O número informado foi: {numero}")
    print()

if __name__ == "__main__":
    main()