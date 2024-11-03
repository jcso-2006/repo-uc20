#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

# Solicita ao usuário que insira o nome de uma cidade
cidade = input("Digite o nome de uma cidade: ").strip()

# Verifica se a cidade começa com "SANTO"
if cidade[:5].upper() == "SANTO":
    print("A cidade começa com 'SANTO'.")
else:
    print("A cidade não começa com 'SANTO'.")