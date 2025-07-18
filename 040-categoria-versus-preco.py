# categoria versus preço - programa 4.8 pg 127
categoria = int(input("Digite a categoria do produto (1, 2, 3, 4 ou 5): "))
if categoria == 1:
    preco = 10.00
else:
    if categoria == 2:
        preco = 18.00
    else:
        if categoria == 3:
            preco = 23.00
        else:
            if categoria == 4:
                preco = 26.00
            else:
                if categoria == 5:
                    preco = 31.00
                else:
                    print("Categoria inválida, digite um valor entre 1 e 5!")
                    preco = 0.00
print(f"O preço do produto da categoria {categoria} é: R$ {preco:6.2f}")                    
