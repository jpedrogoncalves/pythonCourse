# map, partial e GeneratorType
from functools import partial
from types import GeneratorType

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco' : 10.00},
    {'nome': 'Produto 1', 'preco' : 11.09},
    {'nome': 'Produto 3', 'preco' : 14.47},
    {'nome': 'Produto 2', 'preco' : 5.50},
    {'nome': 'Produto 4', 'preco' : 27.42},
]

def aumenta_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_porcento = partial(aumenta_porcentagem, porcentagem=1.1)
# novos_produtos = [{**p, 'preco' : aumentar_dez_porcento(p['preco'])} for p in produtos]

def muda_preco_produtos(produto):
    return {**produto, 'preco' : aumentar_dez_porcento(produto['preco'])}

# map()
novos_produtos = list(map(muda_preco_produtos, produtos))
# novos_produtos = (x for x in produtos) # generator)

print_iter(novos_produtos)

# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))

# verificando se novos_produtos é um generator
# print(isinstance(novos_produtos, GeneratorType)) 
