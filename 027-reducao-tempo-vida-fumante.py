# Programa para calcular o tempo perdido de vida por fumar cigarros - exercício 3.15 pg 114
quantidade_cigarros_fumados_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

# Cálculo do tempo perdido
tempo_perdido = quantidade_cigarros_fumados_por_dia * anos_fumando * 365 * 10  # em minutos
tempo_perdido_em_dias = ((tempo_perdido / 60)) / 24  # convertendo minutos para dias
tempo_perdido_em_anos = tempo_perdido_em_dias / 365  # convertendo dias para anos
print(f"Você perdeu aproximadamente {tempo_perdido_em_anos:.2f} anos OU {tempo_perdido_em_dias:.2f} dias de vida por fumar {quantidade_cigarros_fumados_por_dia} cigarros por dia durante {anos_fumando} anos.")

