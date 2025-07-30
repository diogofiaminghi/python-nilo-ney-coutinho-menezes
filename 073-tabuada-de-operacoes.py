# exercício 5.22 pg 148 - escreva um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.

escolha = 1
while escolha !=5:

    print("ESCOLHA A TABUADA QUE DESEJA IMPRIMIR:")
    print("Adição ......... (1)")
    print("Subtração ...... (2)")
    print("Multiplicação .. (3)")
    print("Divisão ........ (4)")
    print("Sair ........... (5)")

    escolha = int(input("Qual tabuada você deseja? "))

    numero_01 = 1
    numero_02 = 1
    if escolha == 1:
        while numero_01 <= 10:
            numero_02 = 1
            while numero_02 <= 10:
                print(f"{numero_01} + {numero_02} = {numero_01 + numero_02}")
                numero_02 += 1
            numero_01 += 1
    elif escolha == 2:
        while numero_01 <= 10:
            numero_02 = 1
            while numero_02 <= 10:
                print(f"{numero_01} - {numero_02} = {numero_01 - numero_02}")
                numero_02 += 1
            numero_01 += 1
    elif escolha == 3:
        while numero_01 <= 10:
            numero_02 = 1
            while numero_02 <= 10:
                print(f"{numero_01} * {numero_02} = {numero_01 * numero_02}")
                numero_02 += 1
            numero_01 += 1
    elif escolha == 4:
        while numero_01 <= 10:
            numero_02 = 1
            while numero_02 <= 10:
                print(f"{numero_01} / {numero_02} = {numero_01 / numero_02}")
                numero_02 += 1
            numero_01 += 1
    else:
        if escolha == 5:
            exit()
        else:
            print("*** OPÇÃO INVÁLIDA - ESCOLHA DE 1 A 5 ***")