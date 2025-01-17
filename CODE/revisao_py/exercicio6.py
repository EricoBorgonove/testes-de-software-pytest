#Escreva um programa que leia o ano de nascimento de um rapaz 
# e mostre a sua situação em relação ao alistamento militar. ​

#- Se estiver antes dos 18 anos, mostre em 
# quantos anos faltam para o alistamento. ​

#- Se já tiver depois dos 18 anos, 
# mostre quantos anos já se passaram do alistamento. 

ano_nascimento = int (input("Digite o ano de Nascimento: "))

idade = 2025 - ano_nascimento

tempo_alistamento = idade - 18  if idade > 18 else 18-idade 

if idade > 18:
    print (f" Já se passaram {tempo_alistamento} anos.")
else:
    print ("Faltam " + str(tempo_alistamento) + " anos.")