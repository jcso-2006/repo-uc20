#Faça um programa que leia algo pelo teclado e mostre na tela do seu tipo primitivo e todas as informações possíveis sobre ele

valor = input("Digite algo: ")

print(f"O tipo primitivo de {valor} é: {type(valor)}")

print(f"É numérico? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanumérico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"É um espaço? {valor.isspace()}")
