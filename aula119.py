# problema dos parâmetros mutáveis em funções Python

# def adiciona_clientes(nome, lista=[]):
#     lista.append(nome)
#     return lista

"""
    problema: toda vida que a função for chamada sem passar o parâmetro lista,
    o parâmetro será repetido em todas as chamadas da função
    solução: 
"""

def adiciona_clientes(nome, lista=None):
    if lista == None:
        lista = []
    lista.append(nome)
    return lista

#solução 2: 

lista1 = []
cliente1 = adiciona_clientes('luiz', lista1)
adiciona_clientes('João', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('camila')
adiciona_clientes('martins', cliente2)
print(cliente2)
