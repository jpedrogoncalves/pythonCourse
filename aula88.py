# Dictionary Comprehension e Set Comprehension
produto = {
    'nome' : 'Caneta Azul',
    'preco' : 2.3,
    'categoria' : 'Escritório'
}

dc = {
    chave: valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
}
print(dc)

s1 = {2 ** i for i in range(10)}
print(s1)
