# exercício 3.6 - página 100

materia1 = 10
materia2 = 7
materia3 = 9

# minha ideia de verificação de aprovação
aprovado_alternativa_a = materia1 >= 7 and materia2 >= 7 and materia3 >= 7

# alternativa B: usando a função all para verificar se todas as notas são >= 7
# Isso é útil se tivermos muitas matérias e não quisermos escrever cada uma delas manualmente
# A função all retorna True se todos os elementos do iterável forem verdadeiros
# Aqui, estamos verificando se todas as notas são maiores ou iguais a 7
# Se alguma nota for menor que 7, all retornará False
# Isso é uma maneira mais concisa de verificar a aprovação
# Vamos usar uma lista para armazenar as notas e aplicar all
aprovado_alternativa_b = all(nota >= 7 for nota in [materia1, materia2, materia3])

print("Aprovado pela alternativa A:", aprovado_alternativa_a)
print("Aprovado pela alternativa B:", aprovado_alternativa_b)
