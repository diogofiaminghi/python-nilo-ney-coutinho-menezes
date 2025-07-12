# Programa de cálculo do valor total a pagar pelo aluguel de um carro - exercício 3.14 pg 114
km_percorrido = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))
valor_por_dia = 60.0
valor_por_km = 0.15
valor_total = (dias_alugados * valor_por_dia) + (km_percorrido * valor_por_km)
print(f"O valor total a pagar é: R$ {valor_total:.2f}")