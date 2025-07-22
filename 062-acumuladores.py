# exercício 5.11 - pg 143
# escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupança.
# exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

deposito_inicial = float(input("Digite o depósito inicial: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
print()
mes = 1
rendimento_do_mes = 0
rendimento_do_mes_acumulado = 0
saldo_atual = deposito_inicial

while mes <= 24:
    # Calcula o rendimento do mês    
    rendimento_do_mes = (saldo_atual + rendimento_do_mes) * (taxa_juros / 100)
    rendimento_do_mes_acumulado += rendimento_do_mes
    saldo_atual = saldo_atual + rendimento_do_mes

    print(f"Mês {mes}: R$ {saldo_atual:.2f} (Rendimento: R$ {rendimento_do_mes:.2f})")
    print(f"Total ganho com juros: R$ {saldo_atual:.2f} - {deposito_inicial:.2f}")
    print(f"Total ganho com juros - com variável acumuladora: R$ {rendimento_do_mes_acumulado:.2f}")
    print()

    mes += 1