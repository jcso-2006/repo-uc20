#Crie um programa que leia o número inteiro e mostre na tela se ele é PAR ou IMPAR

numero = int(input("Digite um numero inteiro"))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")