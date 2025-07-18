# as quatro operações - exercício 4.10 pg 130
print("CALCULADORA COM AS 4 OPERAÇÕES BÁSICAS:")
num1 = float(input("Digite um número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite outro número: "))
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    print("Operação inválida.")
print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
