# corrija o programa a seguir - exercício 4.16 pg 132

# média = input("Digite a sua média: ")
# if média < 4:
#     print("Reprovado")
# if média < 7:
#     print("Recuperação")
# if média > 7:
#     print("Aprovado")

média = float(input("Digite a sua média: "))
if média < 4:
    print("Reprovado")
elif média < 7:
    print("Recuperação")
else:
    print("Aprovado")
# O programa agora converte a entrada para float e usa elif para evitar múltiplas verificações