#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
num1 = float(input("Digite o preço do numero "))
num2 = (num1 / 100)
print(f"O produto com 5% de desconto é {num1-(num2*5)}")