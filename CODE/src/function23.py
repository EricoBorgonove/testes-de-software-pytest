#Cálculo de juros simples
def calcula_juros(principal, taxa, tempo):
    if principal <= 0 or taxa < 0 or tempo <= 0:
        raise ValueError("Valores inválidos para cálculo de juros.")
    return principal * taxa * tempo / 100