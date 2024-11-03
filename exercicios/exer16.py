#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#ex:
#Digite um número 6.127
#O número 6.127 tem a parte inteira 6.

import math

num1 = float(input("Digite um número: "))
inteira = math.floor(numero)

print(f"O número {num1} tem a parte inteira {inteira}")