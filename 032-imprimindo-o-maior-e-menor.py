# imprimindo o maior e menor número entre três números fornecidos pelo usuário - exercício 4.3 pg 123
numero_maior = 0
numero_menor = 0

numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))
numero_c = int(input("Digite o terceiro número: "))

if numero_a > numero_b and numero_a > numero_c:
    numero_maior = numero_a
    if numero_b < numero_c:
        numero_menor = numero_b
    else:
        numero_menor = numero_c
if numero_b > numero_a and numero_b > numero_c:
    numero_maior = numero_b
    if numero_a < numero_c:
        numero_menor = numero_a
    else:
        numero_menor = numero_c
if numero_c > numero_a and numero_c > numero_b:
    numero_maior = numero_c
    if numero_a < numero_b:
        numero_menor = numero_a
    else:
        numero_menor = numero_b
print(f"O maior número é: {numero_maior}")
print(f"O menor número é: {numero_menor}")