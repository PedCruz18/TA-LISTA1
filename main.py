from funcoes import soma, multiplica, duplicados, impares, pares, primos

def main():
    numeros = []
    print()
    print("Digite números inteiros (0 para encerrar):")
    while True:
        try:
            n = int(input("Número: "))
            if n == 0:
                break
            numeros.append(n)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    
    print("\n--- Números escolhidos ---")

    if not numeros:
        print("⚠️ Nenhum número foi escolhido. Encerrando o programa.")
        print()
        quit() # encerrar o programa se não tiver números.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    print(f"✅ Você escolheu: {numeros}")

    print("\n--- Resultados ---")
    print(f"Soma dos números: {soma(numeros)}")
    print(f"Multiplicação dos números: {multiplica(numeros)}")
    print(f"Números duplicados: {duplicados(numeros)}")
    print(f"Números ímpares distintos: {impares(numeros)}")
    print(f"Números pares distintos: {pares(numeros)}")
    print(f"Números primos: {primos(numeros)}") 
    print()

if __name__ == "__main__":
    main()
