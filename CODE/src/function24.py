import math
#Validação de placa de carro (formato brasileiro)

def valida_placa(placa):
    if len(placa) != 7 or not (placa[:3].isalpha() and placa[3:].isdigit()):
        raise ValueError("Placa inválida.")
    return True