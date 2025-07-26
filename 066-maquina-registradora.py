#exercício 5.15 - pg 145
# escreva um programa paar controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e
# a quantidade comprada. Utilize a tabela de códigos a seguir para obter o preço de cada produto
# seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem de 
# erro "Código Inválido"

#codigo_1 = 0.5
#codigo_2 = 1.0
#codigo_3 = 4.0
#codigo_5 = 7.0
#codigo_9 = 8.0

total_itens = 0
total_a_pagar = 0
codigo_invalido = True

while True:
    
    while codigo_invalido == True:
        codigo_invalido = False
        codigo = int(input("Digite o código do seu produto ou 0 para sair: "))
        if codigo == 0:
            print("**************************************************************")
            print(f"Você comprou {total_itens} itens.")
            print(f"O valor total da compra é R$ {total_a_pagar:.2f}.")
            print("**************************************************************")
            exit()
        if codigo != 1 and codigo !=2 and codigo != 3 and codigo != 5 and codigo != 9:
            print("Código Inválido")
            codigo_invalido = True

    codigo_invalido = True
    quantidade = int(input("Digite a quantidade comprada: "))
    
    if codigo == 1:
        preco = 0.5
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.0
    elif codigo ==5:
        preco = 7.0
    elif codigo == 9:
        preco = 8.0

    total_itens += quantidade
    total_a_pagar += quantidade * preco
