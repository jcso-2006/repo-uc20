#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável para verificar se é primo
eh_primo = True

# Verifica se o número é menor que 2
if numero < 2:
    eh_primo = False
else:
    # Verifica se o número tem divisores além de 1 e ele mesmo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break  # Sai do loop se encontrar um divisor

# Exibe o resultado
if eh_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")