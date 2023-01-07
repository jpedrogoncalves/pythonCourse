# interpolação de strings
# s  - string
# d e i  - int
# f  - float
# x e X  - Hexadecimal (ABCDEF0123456789)
nome = 'João'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
# hexa:
print('o hexadecimal de %d é: %08X' % (1500, 1500))
