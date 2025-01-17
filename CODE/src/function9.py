from function8 import gcd

def lcm(a, b):
    """Calcula o mínimo múltiplo comum (LCM)."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)