# exercício 5.19 - pg146 - contagem de cedulas - agora com moedas de 1, 2, 5, 10 e 50 centavos;

from decimal import Decimal, getcontext

# Define precisão suficiente
getcontext().prec = 10

valor = Decimal('0.0')

while valor < Decimal('0.01'):
    valor = Decimal(input("Digite o valor a pagar: "))

cedulas = 0
atual = Decimal('100.00')
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R$ {atual}")
        if apagar == Decimal('0.00'):
            break
        if atual == Decimal('100.00'):
            atual = Decimal('50.00')
        elif atual == Decimal('50.00'):
            atual = Decimal('20.00')
        elif atual == Decimal('20.00'):
            atual = Decimal('10.00')
        elif atual == Decimal('10.00'):
            atual = Decimal('5.00')
        elif atual == Decimal('5.00'):
            atual = Decimal('1.00')
        elif atual == Decimal('1.00'):
            atual = Decimal('0.50')
        elif atual == Decimal('0.50'):
            atual = Decimal('0.10')
        elif atual == Decimal('0.10'):
            atual = Decimal('0.05')
        elif atual == Decimal('0.05'):
            atual = Decimal('0.02')
        elif atual == Decimal('0.02'):
            atual = Decimal('0.01')
        cedulas = 0
