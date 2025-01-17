# Validação de idade
def valida_idade(idade):
    if idade < 0 or idade > 150:
        raise ValueError("Idade deve estar entre 0 e 150.")
    return True