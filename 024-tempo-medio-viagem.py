# tempo médio de viagem - exercicio 3.12 pg 113
distancia_km = float(input("Digite a distância em km: "))
velocidade_media_esperada = float(input("Digite a velocidade média esperada (km/h): "))
tempo_da_viagem_horas = distancia_km / velocidade_media_esperada
print(f"Tempo da viagem estimada: {tempo_da_viagem_horas:.2f} horas")