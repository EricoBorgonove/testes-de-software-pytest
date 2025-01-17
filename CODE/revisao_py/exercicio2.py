# A locadora de carros precisa da sua ajuda para cobrar seus 
# serviços. Escreva um programa que pergunte a quantidade de 
# Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço total a pagar, 
# sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado. 


dias_alugados = int(input("Digite a qtdade de dias: "))
km_percorrido = float (input("Digite a km percorrida: "))

valor_aluguel = (dias_alugados * 90) + (km_percorrido * 0.2)

print (f"O valor do aluguel será R${valor_aluguel:.2f}")