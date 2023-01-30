# empacotamento e desenpacotamento de dicionários + kwargs
a, b = 1, 2
a, b = b, a
# print(a,b)

info_pessoa = {
    'nome' : 'João',
    'sobrenome' : 'Pedro',
}

dados_pessoa = {
    'idade' : 22,
    'altura' : 1.69,
}

# desenpacotamento de dicionário
pessoa = {**info_pessoa, 'chave':1, 'nome':156}
# print(pessoa)

# a, b = pessoa
# print(a,b) # retorna as chaves

# a, b = pessoa.values()
# print(a,b) # retorna os valores, por causa do values()

# a, b = pessoa.items()
# print(a,b) # retorna uma tupla com chave e valor (nome, joao) (sobrenome, pedro)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# args e kwargs
# kwargs - keyword arguments / argumentos nomeados

def mostra_argumentos_nomeados(*args, **kwargs):
    print(args)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostra_argumentos_nomeados(1, 2, nome='João', qlq=123)
mostra_argumentos_nomeados(**pessoa)

config = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}
mostra_argumentos_nomeados(**config)
