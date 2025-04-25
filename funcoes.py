import random

def rolar_dados(x):
    resultados = []
    for _ in range(x):
        resultados.append(random.randint(1, 6))
    return resultados
