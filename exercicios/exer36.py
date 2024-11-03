#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o calor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos ele vai pagar: "))

mensal = valor / (anos * 12)
limite = salario * 0.30

if mensal <= limite:
    print("Empréstimo aprovado!")
    print(f"Valor da prestação mensal: R$ {mensal:.2f}")
else:
    print("Empréstimo negado!")
    print(f"Valor da prestação mensal: R$ {mensal:.2f}, que excede o limite de 30% do salário.")