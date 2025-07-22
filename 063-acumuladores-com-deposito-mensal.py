# exercício 5.12 - pg 143
# altere o programa anterior para que o usuário possa informar um depósito mensal.

deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
deposito_mensal = float(input("Digite o depósito mensal: "))
print()
mes = 1
rendimento_do_mes = 0
rendimento_do_mes_acumulado = 0
saldo_atual = deposito_inicial

while mes <= 24:
    
    # Calcula o rendimento do mês    
    saldo_atual += deposito_mensal
    rendimento_do_mes = (saldo_atual) * (taxa_juros / 100)
    rendimento_do_mes_acumulado += rendimento_do_mes
    saldo_atual += rendimento_do_mes

    print(f"Mês {mes}: R$ {saldo_atual:.2f} (Rendimento: R$ {rendimento_do_mes:.2f})")
    print(f"Total ganho com juros - com variável acumuladora: R$ {rendimento_do_mes_acumulado:.2f}")
    print()

    mes += 1