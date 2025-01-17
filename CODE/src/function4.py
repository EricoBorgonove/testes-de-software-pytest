def factorial(n):
    """Calcula o fatorial de um número."""
    if n < 0:
        raise ValueError("Número deve ser não-negativo.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
