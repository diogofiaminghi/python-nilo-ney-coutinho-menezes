# categoria versus preco usando elif - programa 4.9 pg 129
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
    preco = 10.00
elif categoria == 2:
    preco = 18.00
elif categoria == 3:
    preco = 23.00
elif categoria == 4:
    preco = 26.00
elif categoria == 5:
    preco = 31.00
else:
    preco = 0.00
    print("Categoria inválida, digite um valor entre 1 e 5!")
print(f"O preço do produto da categoria {categoria} é: R$ {preco:6.2f}")