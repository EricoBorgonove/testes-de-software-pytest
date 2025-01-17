# Função de somar números inteiros
def soma_inteiros(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Os parâmetros devem ser números inteiros.")
    return a + b
