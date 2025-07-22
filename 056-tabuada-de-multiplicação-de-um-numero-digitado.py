# imprimir tabuada de multiplicação de um número digitado - exercício 5.6 pg 141

print("TABUADA DE MULTIPLICAÇÃO DE UM NÚMERO DIGITADO")

numero = int(input("Digite um número: "))
x = 1
while x <= 10:
    resultado = numero * x
    print(f"{numero} * {x} = {resultado}")
    x += 1