def transformar_string(texto):
    # Verifica se o texto contém apenas números -> achei relevante colocar isso aqui.
    if texto.isdigit():
        print()
        raise ValueError("Erro: A escrita contém apenas números, não é permitido.")

    # Usando o método title() para deixar a primeira letra de cada palavra maiúscula
    return texto.title()

# Lendo a entrada do usuário
print("""
Bem Vindos ao programa de ler strings.
------------------------------------
By PedCruz.
""")

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
