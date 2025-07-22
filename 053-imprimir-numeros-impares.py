# imprimir de 1 até o número digitado pelo usuário, apenas os números ímpares - exercício 5.4 pg 140

print("NÚMEROS IMPARES DE 1 ATÉ O NÚMERO DIGITADO")

numero = int(input("Digite um número: "))
x = 1
while x <= numero:
    if x % 2 != 0:
        print(x)
    x += 1