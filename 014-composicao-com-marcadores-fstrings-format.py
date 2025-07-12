# exemplo da página 105
nome = "Diogo"
idade = 45
dinheiro = 350.50

print("%s tem %d anos e apenas R$%f no bolso" % (nome, idade, dinheiro))
print("%12s tem %3d anos e apenas R$%5.2f no bolso" % (nome, idade, dinheiro))
print("%12s tem %03d anos e apenas R$%5.2f no bolso" % (nome, idade, dinheiro))
print("%-12s tem %-3d anos e apenas R$%-5.2f no bolso" % (nome, idade, dinheiro))
print("***********************************")

# a forma de composição acima é antiga, mas ainda funciona
# a partir do Python 3.6, podemos usar f-strings para uma sintaxe mais moderna
print(f"{nome} tem {idade} anos e apenas R${dinheiro:.2f} no bolso")
print(f"{nome:12} tem {idade:3} anos e apenas R${dinheiro:5.2f} no bolso")
print(f"{nome:12} tem {idade:03} anos e apenas R${dinheiro:5.2f} no bolso")
print(f"{nome:<12} tem {idade:<3} anos e apenas R${dinheiro:<5.2f} no bolso")
print(f"{nome:>12} tem {idade:>3} anos e apenas R${dinheiro:>5.2f} no bolso")
print(f"{nome:^12} tem {idade:^3} anos e apenas R${dinheiro:^5.2f} no bolso")
print(f"{nome:=^12} tem {idade:=^3} anos e apenas R${dinheiro:=^5.2f} no bolso")
print("***********************************")

# abaixo outra forma de escrever a mesma coisa, mas com o método format
print("{} tem {} anos e apenas R${:.2f} no bolso".format(nome, idade, dinheiro))
print("{2} tem {1} anos e apenas R${0} no bolso".format(nome, idade, dinheiro))
print("{:12} tem {:3} anos e apenas R${:5.2f} no bolso".format(nome, idade, dinheiro))
print("{:12} tem {:03} anos e apenas R${:5.2f} no bolso".format(nome, idade, dinheiro))
print("{:<12} tem {:<3} anos e apenas R${:<5.2f} no bolso".format(nome, idade, dinheiro))
print("{:>12} tem {:>3} anos e apenas R${:>5.2f} no bolso".format(nome, idade, dinheiro))
print("{:^12} tem {:^3} anos e apenas R${:^5.2f} no bolso".format(nome, idade, dinheiro))
print("{:=^12} tem {:=^3} anos e apenas R${:=^5.2f} no bolso".format(nome, idade, dinheiro))
