#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezez aparece a letra 'A'
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ").strip().upper()

# Conta quantas vezes a letra "A" aparece na frase
quantidade_a = frase.count("A")

# Encontra a posição da primeira ocorrência da letra "A"
primeira_posicao = frase.find("A") + 1

# Encontra a posição da última ocorrência da letra "A"
ultima_posicao = frase.rfind("A") + 1

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes na frase.")
print(f"A primeira posição em que aparece é {primeira_posicao}.")
print(f"A última posição em que aparece é {ultima_posicao}.")
