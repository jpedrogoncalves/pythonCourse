"""
listas em python
tipo list = mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
métodos úteis: append, insert, pop, del, clear, extend, +
"""
lista = [10, 20, 30, 40]
print(lista[2])
#del lista[2]  delete o índice 2 (30)
lista.append(50) # adiciona 50 ao final da lista
lista.append(60) # adiciona 60 ao final da lista
lista.append('asdasd') # adiciona 70 ao final da lista
print(lista)
# lista.pop() # remove o ultimo indice da lista. há como saber qual valor foi removido:
# pop() também pode remover o indice que você definir. pop(2)
remov = lista.pop()
print(f'O valor removido foi: {remov}')
print(lista)
