#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-0

num = 0

for i in range(6):
    num1 = int(input("Digite um número inteiro: "))
    if num1 % 2 == 0:
        num += num1

print(f"A soma dos números pares é: {num}")