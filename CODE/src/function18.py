#Validação de CPF
def valida_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF deve ter 11 dígitos.")
    return True