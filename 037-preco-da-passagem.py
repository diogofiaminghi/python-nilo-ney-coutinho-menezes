# preço da passagem
# perguntar a distância a ser percorrida em Km
distancia = int(input("Digite a distância a ser percorrida em Km: "))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço da passagem é R$ {preco:.2f}")
