from funcoes import soma, multiplica, duplicados, impares, pares, primos

def main():
    numeros = []
    print("\nDigite números inteiros (0 para continuar):")
    
    while True:
        try:
            n = int(input("Número: "))
            
            if n == 0:
                if len(numeros) < 2:
                    print("⚠️ Digite pelo menos DOIS números antes de continuar.")
                    continue  # volta pro início do loop
                else:
                    break  # dois ou mais números digitados, podemos seguir
            
            numeros.append(n)

        except ValueError:
            print("❌ Por favor, digite um número inteiro válido.")

    print("\n--- Números escolhidos ---")                                                                                                                                                                                                                                                                                                                                                                                                                                          
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
