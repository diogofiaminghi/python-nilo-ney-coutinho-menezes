# exercício 5.27 - pg 149
# escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se contiua o mesmo caso seus dígitos seja invertidos.
# exemplos: 454 e 10501

print("********** VERIFICANDO SE O NÚMERO É PALÍNDROMO **********")

numero = int(input("Digite o número: "))
numero_invertido = int(str(numero)[::-1])

if numero == numero_invertido:
    print(f"O número {numero} é um palíndromo.")
else:
    print(f"O número {numero} NÃO é um palíndromo")