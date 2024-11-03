#Faça um programa que leia um número e mostre na tela cada um dos digitos separados.
#EX:
#Digite um número: 1834
#Unidade:4
#Dezena:3
#Centena:8
#Milhar:1
numero = input("Digite um número: ")
if len(numero) <= 4 and numero.isdigit():
    numero = numero.zfill(4)
    
    # Obtém cada posição do número
    milhar = numero[0]
    centena = numero[1]
    dezena = numero[2]
    unidade = numero[3]
    
    # Exibe os resultados
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print("Por favor, digite um número de até 4 dígitos.")