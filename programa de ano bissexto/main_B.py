# coloquei um bonûs aqui, se for digitado um ano no futuro, o programa informa usando o verbo "será". 
from datetime import datetime

def eh_bissexto(ano):
    # Um ano só é bissexto se for divisível por 4,
    # exceto se for divisível por 100, a menos que também seja divisível por 400.
    # Curiosidade: já houve o ano 1 na Terra, mas não houve o ano 0. Rs
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def main():
    try:
        print()
        ano = int(input("Digite um ano: "))
        ano_atual = datetime.now().year

        futuro = ano > ano_atual

        if eh_bissexto(ano):
            if futuro:
                print(f"O ano {ano} será bissexto.")
            else:
                print(f"O ano {ano} é bissexto.")
        else:
            if futuro:
                print(f"O ano {ano} não será bissexto.")
            else:
                print(f"O ano {ano} não é bissexto.")
        print()

    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        print()

if __name__ == "__main__":
    main()
