"""
listas
insert - adiciona um item no indice escolhido
clear - limpa a lista
extend - extende a lista
+ - contatena listas
"""
# lista = [1,2,3,4]
# # lista.clear() - limpa a lista
# lista.insert(2, 'aosdjioas')
# print(lista)
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # não é possivel salvar numa variável, pois o extend
# mexe diretamente na lista A

print(lista_a)
print(lista_c)
