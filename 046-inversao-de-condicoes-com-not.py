# inversão de condições com not - exercício 4.13 pg 131
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

if a == b:
    print('Os números são iguais')
else:
    if not (a > b):
        print('b é maior que a')
    elif not (a < b):
        print('a é maior que b')


