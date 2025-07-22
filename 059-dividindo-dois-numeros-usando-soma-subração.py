# divisão de 2 números usando soma ou subtração - exercício 5.9 pg 141

print("DIVISÃO DE DOIS NÚMEROS USANDO SOMA OU SUBTRAÇÃO")

resultado = 0
dividendo = int(input("Digite o primeiro número: "))
divisor = int(input("Digite o segundo número: "))

if dividendo < 0 and divisor > 0:
    dividendo = -dividendo
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1
    resultado = -resultado

elif dividendo > 0 and divisor < 0:
    divisor = -divisor
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1
    resultado = -resultado

elif dividendo < 0 and divisor < 0:
    dividendo = -dividendo
    divisor = -divisor
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1

elif dividendo > 0 and divisor > 0:
    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1

print(f"O resultado da divisão é: {resultado}")
print(f"O resto da divisão é: {dividendo}")