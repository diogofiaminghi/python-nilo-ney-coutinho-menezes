# imprimir tabuada de multiplicação com início e fim definido pelo usuário - exercício 5.7 pg 141

print("TABUADA DE MULTIPLICAÇÃO COM INÍCIO E FIM DEFINIDO PELO USUÁRIO")

numero = int(input("Digite um número: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

while inicio <= fim:
    resultado = numero * inicio
    print(f"{numero} * {inicio} = {resultado}")
    inicio += 1