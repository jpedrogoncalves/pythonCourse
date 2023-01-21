# manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'João Pedro'
print(pessoa[chave])
pessoa['sobrenome'] = 'Alencar'

pessoa[chave] = 'Camila'
print(pessoa[chave])

print(pessoa)

del pessoa['sobrenome']
print(pessoa)

# para ver se 'sobrenome' existe:
# if pessoa.get('sobrenome', None):
#     print('existe')
# maneira certa de usar

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
