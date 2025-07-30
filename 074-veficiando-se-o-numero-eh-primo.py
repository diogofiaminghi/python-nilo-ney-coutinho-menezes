# exercício 5.23 pg 149
# escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa verificação, calcule o resto da divisão
# do número por 2 e depois por todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero, o número
# não é primo. Observe que 0 e 1 não são primos e que 2 é o núnico número primo que é par.

numero = -1

while numero < 0:
    print("****** VERIFICAÇÃO SE O NÚMERO É OU NÃO PRIMO ******")
    numero = int(input("Digite o número: "))

if numero == 0:
    print("O número 0 não é primo!")
    exit()
if numero == 1:
    print("O número 1 não é primo!")
    exit()
if numero == 2:
    print("O número 2 é primo!")
    exit()
else:
    if numero % 2 == 0:
        print(f"O número {numero} não é primo!")
        exit()
    else:
        divisor = 3
        while divisor < numero:
            if numero % divisor == 0:
                print(f"O número {numero} não é primo!")
                exit()
            else:
                divisor += 2
        print(f"O número {numero} é primo!")
        exit()