#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente  de um triangulo retângulo,
#calcule e mostre o comprimento da hipotenusa

import math

oposto = float(input("Digite o valor do cateto oposto: "))
adjacente = float(input("Digite o valor do cateto adjacente: "))

resultado = math.sqrt(oposto**2 + adjacente**2)

print(f"O comprimento hipotenusa do triângulo retângulo {resultado}")