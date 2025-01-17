# Função de raiz quadrada

import math
def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Número negativo não possui raiz quadrada real.")
    return math.sqrt(x)