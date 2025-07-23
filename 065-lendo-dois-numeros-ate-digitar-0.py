# escreva um programa que leia numeros inteiros do teclado. O programa deve ler os números até que o usuário digite 0.
# no final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética

soma = 0
quantidade_de_numeros_digitados = 0

while True:
    
    numero_digitado = int(input("Digite numeros. Querendo sair, digite 0: "))
    if numero_digitado == 0:
        break
    quantidade_de_numeros_digitados += 1
    soma += numero_digitado
    media_aritmetica = soma / quantidade_de_numeros_digitados

print(f"Foram digitados {quantidade_de_numeros_digitados} números.")
print(f"E média aritmética de {soma} por {quantidade_de_numeros_digitados} é igual a {media_aritmetica:.2f}.")

