# exercício 5.26 pg 149
# escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração 
# para calcular o resultado

print("***** CALCULANDO O RESTO DA DIVISÃO INTEIRA *****")
dividendo = float(input("Digite o Dividendo: "))
divisor = float(input("Digite o Divisor: "))

while True:
    auxiliar = dividendo - divisor
    if auxiliar < divisor:
        print(f"O resto da divisão é {auxiliar:.0f}")
        break
    dividendo = auxiliar