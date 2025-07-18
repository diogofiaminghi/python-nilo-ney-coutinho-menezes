# aprovar empréstimo bancáriio - exercício 4.11 pg 130
valor_da_casa = float(input("Qual o valor da casa a ser adquirida? "))
salario_mensal = float(input("Qual o seu salário mensal? "))
anos_pagamento = int(input("Em quantos anos você pretende pagar? "))

prestacao_mensal = valor_da_casa / (anos_pagamento * 12)

if prestacao_mensal > (salario_mensal * 0.3):
    print("Empréstimo não aprovado.")
else:
    print("Empréstimo aprovado.")
    print(f"Valor da prestação mensal: R$ {prestacao_mensal:.2f}")
    print(f"Total a ser pago: R$ {valor_da_casa:.2f}")
    print(f"Prazo de pagamento: {anos_pagamento} anos")
    print(f"Total de prestações: {anos_pagamento * 12} meses")