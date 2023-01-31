# List Comprehension em python
# é uma forma rápida para criar listas a partir de iteráveis
# lista = []
# # for numero in range(10):
# #     lista.append(numero)

# lista = [x * 2 for x in range(10)]
# print(lista)
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome' : 'p1', 'preco' : 10},
    {'nome' : 'p2', 'preco' : 15},
    {'nome' : 'p3', 'preco' : 25},
]

# aumento de 5% em todos os produtos:
# novos_produtos = [{'nome' : produto['nome'], 'preco' : produto['preco'] * 1.05} for produto in produtos]
novos_produtos = [{**produto, 'preco' : produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos if produto['preco'] > 10]

# filtro: inclui algo na lista se a condição do lado DIREIO do for, é verdadeira
# lista = [n for n in range(10) if n < 4]
# print(lista)
p(novos_produtos)
