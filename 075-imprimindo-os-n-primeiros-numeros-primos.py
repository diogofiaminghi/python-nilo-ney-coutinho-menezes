# exercício 5.24 pg 149
# modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

x_primeiros_primos = -1

while numero <= 0:
    print("****** IMPRIMINDO OS N PRIMEIROS NÚMEROS PRIMOS ******")
    x_primeiros_primos = int(input("Digite o número: "))

if x_primeiros_primos == 1:
    print("2")
    exit()

numero_a_ser_testado = 3

