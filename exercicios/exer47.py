#Crie um programa que mostre na tela todos os números pares que estão entre 1 e 100
contador = 1
print("Números pares entre 1 e 100:")

while contador <= 100:
    if contador % 2 == 0:  # Verifica se o número é par
        print(contador)
    contador += 1  # Incrementa o contador

