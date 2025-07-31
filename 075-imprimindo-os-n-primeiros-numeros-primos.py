#exercício 5.23 pg 149
# modifique o programa anterior de forma a ler umnúmero n. Iimprima os n primeiros números primos.

n = int(input("Digite quantos números primos deseja encontrar: "))

contador = 0        # Conta quantos primos já foram encontrados
numero = 2          # Começamos verificando a partir do número 2

while contador < n:
    eh_primo = True
    i = 2
    while i * i <= numero: # Enquanto o quadrado de i for menor ou igual ao número atual, continue testando.
        if numero % i == 0:
            eh_primo = False
            break
        i += 1

    if eh_primo:
        print(numero)
        contador += 1

    numero += 1