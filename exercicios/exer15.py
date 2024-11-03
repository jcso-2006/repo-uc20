#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = 60.00
km = 0.15

alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))
percorridos = float(input("Digite a quantidade de Km percorridos: "))

total = (alugados * dia) + (percorridos * km)

print(f"O preço total é R${total:.2f}")