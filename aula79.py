# sets - conjuntos em python
# sets em python são mutáveis, porém aceitam
# apenas tipos imutáveis como valor interno.
# não tem par de chave e valor

# {} não cria um set vazio, e sim, um dicionário
# não garante a ordem dos elementos
# não permite elementos duplicados
# Não aceitam dados mutáveis, como listas ou até mesmo sets
# tupla pode, com a vírgula no final
# não tem índices
# são iteráveis (for, in, not in)

# criando um set:
# s1 = set('pedro')
# ou:
# s1 = {0, 1, 2, a, 'pedro'}
# print(s1)

# métodos úteis:
# add, update, clear, discard

# l1 = [1, 2, 3, 3, 3, 3, 3, 3, 3, 3]
# s1 = set(l1)
# l2 = list(s1)
# print(l2)
# s1 = set()
# s1.add('João')
# s1.add(1)
# # s1.update('Olá mundo') - adiciona de forma iterada
# # pra adicionar de forma normal com o update:
# s1.update(('Olá mundo')) # adicionando uma tupla
# print(s1)
# # s1.clear() # limpa o set
# s1.discard('Olá mundo') # precisa de um valor a ser descartado
# print(s1)

# operadores úteis:
# união | união (union) - une (tira valores duplicados)
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que não estão em ambos
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)
s3 = s1 ^ s2
print(s3)
