#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Exemplo: Ana Maria de Souza
#primeiro: Ana
#último: Souza

# Solicita ao usuário que insira o nome completo
nome_completo = input("Digite seu nome completo: ").strip()

# Divide o nome em partes
nomes = nome_completo.split()

# Exibe o primeiro e o último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
