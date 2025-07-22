# multiplicação de 2 números usando soma ou subtração - exercício 5.8 pg 141

print("MULTIPLICAÇÃO DE DOIS NÚMEROS USANDO SOMA OU SUBTRAÇÃO")

resultado = 0
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

while numero2 > 0:
    resultado = resultado + numero1
    numero2 -= 1

print(f"O resultado da multiplicação é: {resultado}")