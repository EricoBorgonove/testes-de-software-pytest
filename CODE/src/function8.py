def gcd(a, b):
    """Calcula o máximo divisor comum (GCD)."""
    while b:
        a, b = b, a % b
    return a