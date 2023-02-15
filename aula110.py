# combinations, permutations e product - itertools
# combinação - ordem não importa - iterável + tamanho do grupo
# permutação - ordem importa
# produto - ordem importa e repete valores únicos
from itertools import combinations, permutations, product
pessoas = [
    'João', 'Pedro', 'Camila', 'Martins',
]

camisetas = [
    ['preta', 'branca',],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

def print_iterator(iterator):
    print(*list(iterator), sep='\n')

# combinations(iter, int)
# combinacao = combinations(pessoas, 2)
# print_iterator(combinacao)
# print('-'*100)
# permutacao = permutations(pessoas, 2)
# print_iterator(permutacao)
# print('-'*100)
produto = product(*camisetas)
print_iterator(produto)
