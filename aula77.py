"""
métodos úteis dos dicionários:
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com os valores
    items - iterável com chaves e valores
    setdefault - adiciona valor se a chave não existe
    copy - retorna uma cópia rasa (shallow copy)
    get - obtém uma chave
    pop - apaga um item com a chave selecionada (del) e retorna o valor
    popitem - apaga o ultimo item adicionado
    update - atualiza um dicionário com outro
"""
# pessoa = {
#     'nome': 'João Pedro',
#     'sobrenome' : 'Alencar',
# }

# # print(pessoa.__len__())
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))
# pessoa.setdefault('idade', 19)

# print(pessoa['idade']) # daria erro, se não fosse o setdefault
# import copy

# d1 = {
#     'c1' : 1,
#     'c2' : 2,
#     'l1' : [0, 1, 2],
# }

# # d2 = d1.copy() # copia todos os dados imutáveis, porém os mutáveis continuam apontando para o mesmo endereço da memória
# d2 = copy.deepcopy(d1) # aqui entra em todos os subniveis
# d2['l1'][1] = 912032

# d2['c1'] = 356161651
# print(d1)
# print(d2)
p1 = {
    'nome' : 'João',
    'idade' : 21
}
# print(p1.get('nome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
p1.update(
    {
        'nome' : 'João Pedro',
        'sobrenome' : 'alencar',
    }
)
print(p1)
