# variáveis livres + nonlocal (locals, globals)
# print(*globals(), sep='\n')
# def fora(x):
#     a = x

#     def dentro():
#         print(locals())
#         return a # a é a variável livre
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(201)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        # pra evitar erro, usamos o 'nonlocal' para 'puxar' a variável de fora do escopo de interna
        nonlocal valor_final
        valor_final += valor_a_concatenar # gera erro, pois a variavel não é do escopo
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
