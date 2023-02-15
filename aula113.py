# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco' : 10.00},
    {'nome': 'Produto 1', 'preco' : 11.09},
    {'nome': 'Produto 3', 'preco' : 104.47},
    {'nome': 'Produto 2', 'preco' : 5.50},
    {'nome': 'Produto 4', 'preco' : 27.42},
]

# novos_produtos = [p for p in produtos if p['preco'] > 10]
# filter(funcao, iteravel)
novos_produtos = filter(lambda p: p['preco'] > 100, produtos)
# retorna sempre a mesma quantidade ou menor que a original e até mesmo nada
print_iter(novos_produtos)
