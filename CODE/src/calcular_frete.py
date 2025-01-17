#1 Criar a Função:

#  Até 100 km: R$5,00 fixo mais R$0,10 por kg.
#  Entre 101 e 500 km: R$10,00 fixo mais R$0,20 por kg.
#  Acima de 500 km: R$20,00 fixo mais R$0,30 por kg.

def calculo_frete (distancia: int , peso: float) -> float:

    if distancia > 0 and distancia <= 100:
        tarifa = 5
        custo_peso = 0.1
    elif distancia >= 101 and distancia <= 500:
        tarifa = 10
        custo_peso = 0.2
    elif distancia >= 501:
        tarifa = 20
        custo_peso = 0.3
    else:
        raise ValueError("distância incorreta")
    return (tarifa * distancia + peso* custo_peso)