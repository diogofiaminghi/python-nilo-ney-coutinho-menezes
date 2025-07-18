# reescrever com if, elif e else - exercício 4.14 - página 131
# if a < 10:
#     print('a é menor que 10')
# if a >= 10 and a < 20:
#     print('a é maior ou igual a 10 e menor que 20')
# if a >= 20:
#     print('a é maior ou igual a 20')

a = int(input('Digite um número: '))

if a < 10:
    print('O número é menor que 10')
elif a >= 10 and a < 20:
    print('O número é maior ou igual a 10 e menor que 20')
else:
    print('O número é maior ou igual a 20')
