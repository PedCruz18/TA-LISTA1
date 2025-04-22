def soma(lista):
    return sum(lista)

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
    return list(set([num for num in lista if num % 2 != 0]))

def pares(lista):
    return list(set([num for num in lista if num % 2 == 0]))

def primos(lista):
    def eh_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in set(lista) if eh_primo(num)]
