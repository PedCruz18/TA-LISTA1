def transformar_string(texto):
    # Verifica se o texto contém apenas números -> achei relevante colocar isso aqui.
    # Verifica se o texto contém apenas números
    if texto.isdigit():
        print()
        raise ValueError("Erro: A escrita contém apenas números, não é permitido.")


    # Lista de palavras que não devem ter a primeira letra maiúscula
    excecoes = {"é", "a", "as", "o", "os", "da", "das", "de", "do", "dos", "em", "para", "com", "sem", "sobre", "entre"}

    # Dividindo o texto em palavras
    palavras = texto.split()

    # Transformando a primeira palavra em maiúscula e as outras conforme necessário
    resultado = []

    for i, palavra in enumerate(palavras):
        # Se a palavra não for uma exceção, coloca a primeira letra em maiúscula
        if palavra.lower() not in excecoes or i == 0:
            resultado.append(palavra.capitalize())
        else:
            resultado.append(palavra.lower())

    # Unindo as palavras de volta em uma string
    return " ".join(resultado)

# Lendo a entrada do usuário
print()
entrada = input("Digite uma frase: ")


try:
    # Transformando a string
    resultado = transformar_string(entrada)
    # Imprimindo o resultado
    print(resultado)
    print()
except ValueError as e:
    # Exibindo o erro se a entrada contiver apenas números
    print(e)
    print()
