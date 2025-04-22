# Aqui foi um desafio em tanto!
# O código foi reescrito para usar comprehensions.

from funcoes2 import soma, multiplica, duplicados, impares, pares, primos

def ler_numeros(numeros=None):
    if numeros is None:
        numeros = []

    try:
        # Solicita um número ao usuário
        n = int(input("Número: "))

        # Caso o número seja 0, finaliza a coleta de números
        if n == 0:
            if len(numeros) < 2:
                # Se a lista tem menos de 2 números, pergunta se o usuário quer continuar
                if len(numeros) == 1:
                    confirmacao = input(f"Você tem certeza que deseja continuar com o número único {numeros[0]}? (s/n): ").lower()
                    if confirmacao == 's':
                        return numeros  # Retorna a lista com um único número
                    else:
                        print("Vamos continuar adicionando números então.")
                        return ler_numeros(numeros)  # Permite que o usuário adicione mais números
                else:
                    print("⚠️  Digite pelo menos UM número antes de continuar.")
                return ler_numeros(numeros)  # Volta a pedir números, pois não tem 2 números ainda.

            return numeros  # Retorna a lista quando a condição de pelo menos 2 números for atendida

        # Se o número não for 0, adiciona o número à lista e continua pedindo
        return ler_numeros(numeros + [n])

    except ValueError:
        print("❌  Por favor, digite um número inteiro válido.")
        return ler_numeros(numeros)  # Em caso de erro, pede novamente um número


def main():

    print("""
    Bem Vindos ao programa de resultados.
    ------------------------------------
    By PedCruz.
    """)


    print("\nDigite números inteiros (0 para continuar):")
    numeros = ler_numeros()

    print("\n--- Números escolhidos ---")
    print(f"✅ Você escolheu: {numeros}")

    print("\n--- Resultados ---")
    print(f"📌 Soma dos números: {soma(numeros)}")
    print(f"📌 Multiplicação dos números: {multiplica(numeros)}")
    print(f"📌 Números duplicados: {duplicados(numeros)}")
    print(f"📌 Números ímpares distintos: {impares(numeros)}")
    print(f"📌 Números pares distintos: {pares(numeros)}")
    print(f"📌 Números primos: {primos(numeros)}")
    print()

if __name__ == "__main__":
    main()
