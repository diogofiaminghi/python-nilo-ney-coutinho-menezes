# Programa para verificar se o carro está acima do limite de velocidade e calcular a multa - exercício 4.2 - pg 121
velocidade_atual = int(input("Digite a velocidade atual do carro: "))
limite_velocidade = 80
multa_por_km = 5.0  # Valor da multa por km acima do limite
if velocidade_atual > limite_velocidade:
    print("Multado! Excesso de velocidade.")
    valor_multa = (velocidade_atual - limite_velocidade) * multa_por_km
    print(f"Valor da multa: R$ {valor_multa:.2f}")
else:
    print("Velocidade dentro do limite. Sem multa. Parabéns!")