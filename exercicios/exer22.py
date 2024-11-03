#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = input("Digite seu nome completo: ")

# O nome com todas as letras maiúsculas
print("Nome em maiúsculas:", nome.upper())

# O nome com todas as letras minúsculas
print("Nome em minúsculas:", nome.lower())

# Quantas letras ao todo (sem considerar espaços)
total_letras = len(nome.replace(" ", ""))
print("Total de letras (sem espaços):", total_letras)

# Quantas letras tem o primeiro nome
primeiro = nome.split()[0]
primeiro = len(primeiro)
print("Quantidade de letras do primeiro nome:", primeiro)