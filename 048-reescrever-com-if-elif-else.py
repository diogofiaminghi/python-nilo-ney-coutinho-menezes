# reescreva o pograma a seguir com if-elif-else - exercício 4.15 pg 132

# hora = int(input('Digite a hora atual: '))
# if hora < 12:
#     print('Bom dia!')
# if hora >= 12 and hora <= 18:
#     print('Boa tarde!')
# if hora > 18:
#     print('Boa noite!')

hora = int(input('Digite a hora atual: '))
if hora < 12:
    print('Bom dia!')
elif hora >= 12 and hora <= 18:
    print('Boa tarde!')
else:
    print('Boa noite!')