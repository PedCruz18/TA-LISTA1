def soma(lista):
    # Calcula e retorna a soma dos elementos da lista
    return sum(lista)

def multiplica(lista):
    # Caso a lista não esteja vazia, multiplica o primeiro número pelo resultado da multiplicação dos outros
    return lista[0] * multiplica(lista[1:]) if lista else 1  # Caso a lista esteja vazia, retorna 1 (base da recursão)

# CONFESSO, para mim essa foi a mais difícil de todas as outras funções! ---------------
def duplicados(lista):
    vistos = set()  # Conjunto para armazenar os números já vistos
    repetidos = {num for num in lista if lista.count(num) > 1 and num not in vistos and not vistos.add(num)}
    
    # Retorna os duplicados se existirem, caso contrário retorna uma lista vazia
    return list(repetidos) if repetidos else []
# --------------------------------------------------------------------------------------

def impares(lista):
    # Retorna uma lista de números ímpares encontrados na lista, usando set para garantir que sejam únicos
    return list({x for x in lista if x % 2 != 0})

def pares(lista):
    # Retorna uma lista de números pares encontrados na lista, usando set para garantir que sejam únicos
    return list({x for x in lista if x % 2 == 0})

def primos(lista):
    # Função lambda para verificar se um número é primo
    quando_primo = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    # Retorna uma lista de números primos encontrados na lista
    return list({x for x in lista if quando_primo(x)})
