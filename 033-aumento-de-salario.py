# aumento de salário - exercício 4.4 pg 123
salario = float(input("Digite o seu salário: "))
if salario > 1250:
    salario_com_aumento = salario * 1.10
    print(f"Seu salário com aumento é: R$ {salario_com_aumento:.2f}")
else:
    salario_com_aumento = salario * 1.15
    print(f"Seu salário com aumento é: R$ {salario_com_aumento:.2f}")