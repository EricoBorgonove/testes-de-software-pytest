# Multiplicação com limite
def multiplica_com_limite(a, b, limite):
    resultado = a * b
    if resultado > limite:
        raise ValueError("Resultado excede o limite permitido.")
    return resultado