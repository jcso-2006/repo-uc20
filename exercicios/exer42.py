#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo sera formado:
#Equilatero: todos os lados são iguais
#Isóceles: dois lados são iguais
#Escaleno: todos os lados diferentes

def verifica_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))

if (a + b > c) and (a + c > b) and (b + c > a ):
    print("Ele é um  triângulo")
    if a == b == c:
        tipo = "Equilátero"
    elif a == b or a == lado3 or b == c:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    print(f"Do tipo: {tipo}")
else:
    print("Não é um triângulo")