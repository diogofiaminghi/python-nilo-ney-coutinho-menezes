# corrigindo teste de múltipla escolha - pg 141

print("CORRIGINDO TESTE DE MÚLTIPLA ESCOLHA")
pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Qual é a resposta da questão {questao}?: ")
    if questao == 1 and (resposta == "b" or resposta == "B"):
        pontos += 1
    if questao == 2 and (resposta == "a" or resposta == "A"):
        pontos += 1
    if questao == 3 and (resposta == "d" or resposta == "D"):
        pontos += 1
    questao += 1
print(f"Você fez {pontos} pontos.")