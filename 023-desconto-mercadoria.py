# desconto no preço de mercadoria - exercício 3.11 pg 113
preco_original_mercadoria = float(input("Digite o preço original da mercadoria: "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))
preco_com_desconto = preco_original_mercadoria * (1 - desconto_percentual / 100)
print(f"O desconto foi de R$ {preco_original_mercadoria - preco_com_desconto:.2f}")
print(f"O preço a pagar é de R$ {preco_com_desconto:.2f}")