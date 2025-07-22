# imprimir tabuada de adição de um número digitado - pg 141

print("TABUADA DE ADIÇÃO DE UM NÚMERO DIGITADO")

numero = int(input("Digite um número: "))
x = 1
while x <= 10:
    resultado = numero + x
    print(f"{numero} + {x} = {resultado}")
    x += 1