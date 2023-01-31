# List Comprehension em python
# é uma forma rápida para criar listas a partir de iteráveis
lista = []
# for numero in range(10):
#     lista.append(numero)

lista = [x * 2 for x in range(10)]
# print(lista)

#mapeamento: pegar dados de uma lista, transformar e jogar em outra

produtos = [
    {'nome' : 'p1', 'preco' : 10},
    {'nome' : 'p2', 'preco' : 15},
    {'nome' : 'p3', 'preco' : 25},
]

# aumento de 5% em todos os produtos:
# novos_produtos = [{'nome' : produto['nome'], 'preco' : produto['preco'] * 1.05} for produto in produtos]
novos_produtos = [{**produto, 'preco' : produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} for produto in produtos]

print(*novos_produtos, sep='\n') # desempacotando a lista
