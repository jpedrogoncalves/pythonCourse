# Argumentos nomeados e Argumentos não-nomeados em funções Python
# Argumento nomeado tem nome com sinal de igual
# Argumento não nomeado recebe apenas o argumento (valor)

#        Parâmetros
def soma(x, y, z):
    print(f'{x=}, {y=}, {z=} | x + y + z = {x+y+z}')

# Argumentos: 1, 2
soma(1, 2, 3) # aparece None, pq a função por padrão retorna None
soma(y=2,x=1, z=1) # argumento nomeado
# qualquer argumento depois do argumento nomeado, também tem que ser nomeado (keyword argument)
soma(1, z=2, y=4)
