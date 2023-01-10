# enumerate: enumera iteráveis (índices)
lista = ['João', 'Camila', 'Laura']
lista.append('Aluashd')

lista_enumerada = enumerate(lista) # gera um iterator (ou seja, podemos usar next())
# porém, isso gasta todos os iteráveis, ou seja, se for salvar na variável
# só pode usar uma única vez.

# for item in lista_enumerada:
#     print(item)

for indice, nome in lista_enumerada:
    print(indice, nome)
