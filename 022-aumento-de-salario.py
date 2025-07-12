# aumento de salário - exercicio 3.10 pg 113
salario = float(input("Digite o salário do funcionário: "))
aumento_percentual = float(input("Digite a porcentagem de aumento: "))
salario_novo = salario * (1 + aumento_percentual / 100)
aumento_em_reais = salario_novo - salario
print(f"O aumento foi de R$ {aumento_em_reais:.2f}")
print(f"O novo salário é R$ {salario_novo:.2f}")
print(f"O salário com aumento de {aumento_percentual:.2f}% é R$ {salario_novo:.2f}")