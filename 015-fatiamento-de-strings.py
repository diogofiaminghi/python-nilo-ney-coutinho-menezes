# Fatiamento de Strings - pg 107
s = "ABCDEFGHI"
print(s[:])  # ABCDEFGHI - do início ao final - faz uma cópia da string
print(s[0:2])  # AB - posição 0 inclusa, posição 2 exclusiva
print(s[2:5])  # CDE - posição 2 inclusa, posição 5 exclusiva
print(s[2:])   # CDEFGHI - posição 2 inclusa, até o final
print(s[:5])   # ABCDE - do início até a posição 5 exclusiva
print(s[::2])  # ACEG - do início ao final, pulando de 2 em 2
print(s[::-1]) # IHGFEDCBA - do final ao início, pulando de 1 em 1
print(s[::-2]) # IGECA - do final ao início, pulando de 2 em 2
print(s[1:8:3]) # BDF - do início ao final, começando na posição 1, até a posição 8 exclusiva, pulando de 3
print(s[1:8:2]) # BDFH - do início ao final, começando na posição 1, até a posição 8 exclusiva, pulando de 2
print(s[1:8:1]) # BCDEFGH - do início ao final, começando na posição 1, até a posição 8 exclusiva, pulando de 1
print(s[1:8:4]) # BDFH - do início ao final, começando na posição 1, até a posição 8 exclusiva, pulando de 4
 