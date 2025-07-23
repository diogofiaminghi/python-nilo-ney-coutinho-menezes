# escreva um programa que pergunte o valor inicial de uma dívida e o juros mensal. Pergunte tb o valor mensal que será pago.
# Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
# exercício 5.13 pg 144

print("**************************************************************")
valor_inicial_da_divida = float(input("Digite o valor inicial da dívida: "))
juros_mensal = float(input("Digite o juros mensal em %: "))
pagamento_mensal = float(input("Qual o valor que será pago mensalmente? "))
print("**************************************************************")

juros_primeiro_mes = (valor_inicial_da_divida * (juros_mensal / 100))
if pagamento_mensal <= juros_primeiro_mes:
    print(f"O pagamento_mensal de R$ {pagamento_mensal} precisa ser maior que R$ {juros_primeiro_mes}.")
    exit()

numero_de_meses_para_pagar_a_divida = 0
valor_atual_da_divida = 0.0
valor_atual_da_divida = valor_inicial_da_divida
valor_total_pago = 0.0
valor_total_dos_juros = 0.0

while valor_atual_da_divida > 0:
    numero_de_meses_para_pagar_a_divida += 1
    valor_total_dos_juros = valor_total_dos_juros + (valor_atual_da_divida * (juros_mensal / 100))
    valor_atual_da_divida *= (1 + (juros_mensal / 100))
    valor_atual_da_divida -= pagamento_mensal
    valor_total_pago += pagamento_mensal
    
    print(f"Com {numero_de_meses_para_pagar_a_divida} meses, a evolução da sua dívida é a seguinte:")
    print(f"O valor total pago foi de R$ {valor_total_pago:.2f}")
    print(f"O total de juros pagos foi de R$ {valor_total_dos_juros:.2f}")
    print(f"O valor atual da dívida é {valor_atual_da_divida:.2f}")
    print("**************************************************************")

