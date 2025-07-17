# calculo mensalidade plano celular - programa 4.4 pg 123
plano = input("Qual é o seu plano de celular? ")
if plano == "falopouco":
    minutos_do_plano = 100
    extra = 0.20
    preco = 50
if plano == "falomuito":
    minutos_do_plano = 500
    extra = 0.15
    preco = 99
if plano != "falopouco" and plano != "falomuito":
    print("Não conheço este plano.")
if plano == "falopouco" or plano == "falomuito":
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do Plano é R$ {preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_do_plano:
        suplemento = extra * (minutos_consumidos - minutos_do_plano)
    print(f"Suplemento       R$ {suplemento:10.2f}")
    print(f"Total            R$ {preco + suplemento:10.2f}")
    print("Obrigado por usar nossos serviços!")
