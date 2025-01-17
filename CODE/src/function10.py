def fibonacci(n):
    """Retorna o n-ésimo número de Fibonacci."""
    if n < 0:
        raise ValueError("Número deve ser não-negativo.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a