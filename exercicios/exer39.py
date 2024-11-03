#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo de alistamento

#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

nascimento = int(input("Digite o ano de nascimento: "))
atual = datetime.now().year
idade = atual - nascimento

if idade < 18:
    faltando = 18 - idade
    print(f"Você ainda vai se alistar ao serviço militar. Faltam {faltando} anos.")
elif idade == 18:
    print("É a hora de se alistar ao serviço militar.")
else:
    atraso = idade - 18
    print(f"Já passou do tempo de alistamento. Você está {atraso } anos atrasado.")