"""
cuidados com dados mutáveis:
    = -> copiando o valor (imutáveis)
    = -> aponta para o mesmo lugar da memória (mutáveis)
"""
lista_a = ['Luiz', 'João']
# lista_b = lista_a # as duas apontam para o mesmo lugar da memória!
lista_b = lista_a.copy()

lista_a[0] = 'uasudhas'
print(lista_a, lista_b)
