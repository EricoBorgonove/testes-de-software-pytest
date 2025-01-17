# Validação de número de telefone
def valida_telefone(telefone):
    if len(telefone) != 10 or not telefone.isdigit():
        raise ValueError("Número de telefone inválido.")
    return True