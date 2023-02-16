# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco' : 10.00},
    {'nome': 'Produto 1', 'preco' : 22},
    {'nome': 'Produto 3', 'preco' : 2},
    {'nome': 'Produto 2', 'preco' : 6},
    {'nome': 'Produto 4', 'preco' : 4},
]

# reduce(funcao, iteravel, valor_inicial)
def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(funcao_do_reduce, produtos, 0)
print('total: ', total)

# for p in produtos:
#     total += p['preco']

# #maneira mais resumida
# print(sum([p['preco'] for p in produtos]))

# print(total)
