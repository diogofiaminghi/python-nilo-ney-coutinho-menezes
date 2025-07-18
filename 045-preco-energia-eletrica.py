# preço energia elétrica - exercício 4.12 - pg 130
consumo = float(input('Consumo em kWh: '))
tipo_de_instalacao = input('Tipo de instalação (R, I ou C): ').upper()
if tipo_de_instalacao == 'R':
    if consumo <= 500:
        preco = consumo * 0.40
    else:
        preco = consumo * 0.65
elif tipo_de_instalacao == 'I':
    if consumo <= 5000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
elif tipo_de_instalacao == 'C':
    if consumo <= 1000:
        preco = consumo * 0.55
    else:
        preco = consumo * 0.60
else:
    print('Tipo de instalação inválido.')
    preco = 0
if preco > 0:
    print(f'O preço a pagar é: R$ {preco:.2f}')