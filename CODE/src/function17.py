# Verificar se é par
def eh_par(n):
    if not isinstance(n, int):
        raise ValueError("O número deve ser inteiro.")
    return n % 2 == 0