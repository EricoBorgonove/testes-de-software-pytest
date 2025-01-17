#Cálculo de IMC
def calcula_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    return peso / (altura ** 2)