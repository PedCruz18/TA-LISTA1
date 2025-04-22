def soma(lista):
    resultado = 0
    for num in lista:
        resultado += num
    return resultado

def multiplica(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def duplicados(lista):
    vistos = set()
    repetidos = set()
    for num in lista:
        if num in vistos:
            repetidos.add(num)
        else:
            vistos.add(num)
    return list(repetidos)

def impares(lista):
    impares_lista = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            impares_lista.append(lista[i])
        i += 1
    return impares_lista

def pares(lista):
    pares_lista = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            pares_lista.append(lista[i])
        i += 1
    return pares_lista

def primos(lista):
    def eh_primo(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    primos_lista = []
    for num in lista:
        if eh_primo(num):
            primos_lista.append(num)
    return primos_lista
