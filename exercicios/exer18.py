#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

angulo = float(input("Digite um ângulo em graus: "))
angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"O ângulo de {angulo} graus tem")
print(f"Seno {seno}")
print(f"Cosseno {cosseno}")
print(f"Tangente {tangente}")