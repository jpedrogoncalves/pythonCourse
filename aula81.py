"""
função lambda:
    A função lambda, é uma função como qualquer outra.
    Porém, são funções anônimas que contém apenas uma linha.
    Ou seja, tudo deve ser em uma única expressão.
"""
lista = [
    {'nome' : 'João', 'sobrenome' : 'Pedro'},
    {'nome' : 'Camila', 'sobrenome' : 'Martins'},
    {'nome' : 'Rinaldo', 'sobrenome' : 'Gonçalves'},
    {'nome' : 'Laura', 'sobrenome' : 'Alencar'},
    {'nome' : 'Cristina', 'sobrenome' : 'Alencar'},
]

# python usa a tabela unicode pra fazer ordenação das letras.

# def ordena(item):
#     return item['nome']

# lista.sort(key=ordena)
# print(lista)
# lista.sort(key=lambda item: item['nome'])
# print(lista)

def exibir(lista):
    for item in lista:
        print(item)

l1 = sorted(lista, key=lambda item: item['nome']) # retorna uma cópia rasa da lista 'lista'
l2 = sorted(lista, key=lambda item: item['sobrenome'])

print('NOME:')
exibir(l1)
print('SOBRENOME:')
exibir(l2)
