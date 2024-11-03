#Crie um programa que leie uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços.

frase = input("Digite uma frase: ")
frase = frase.replace(" ", "").lower()
if frase == frase[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")