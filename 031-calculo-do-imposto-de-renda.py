# calculo do imposto de renda - programa 4.3 pg 121
salario = float(input("Digite o salário para o cálculo do imposto: "))
base = salario
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: {salario:6.2f} - Imposto a Pagar: {imposto:6.2f}")
