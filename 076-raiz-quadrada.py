# exercício 5.25 pg 149
# escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo n
# o número a obter a raiz quadrada, considere a base b=2. Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o qudrado de p.
# A cada passo, faça b=p e recalcule p usndo a fórmula apresentada. Para quando a diferença absoluta entre n e o quadrado de p for menor
# que 0,0001.

# "b" Esse é o chute inicial (ou estimativa inicial) para a raiz. É o valor inicial que vamos melhorar a cada passo.

print("********** VAMOS CALCULAR A RAIZ QUADRADA **********")
n = float(input("Você quer saber a raiz quadrada de... : "))

b = 2
diferenca_absoluta = 1
contador = 0

while diferenca_absoluta > 0.0001:
    p = (b + (n / b)) / 2
    quadrado_de_p = p * p
    b = p
    diferenca_absoluta = abs(n - quadrado_de_p)
    contador += 1

print(f"A raiz quadrada de {n} é {p:.2f}! Tivemos {contador} ciclos de calculo para chegar neste resultado!")

