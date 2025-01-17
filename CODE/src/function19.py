import math

# Cálculo de desconto em compras
def calcula_desconto(valor, percentual):
    if valor < 0 or percentual < 0 or percentual > 100:
        raise ValueError("Valor ou percentual inválido.")
    return valor - (valor * percentual / 100)