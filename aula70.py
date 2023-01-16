"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# lembre-te de desempacotamento
# x, y, *resto = 1,2,3,4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total
    # print('args: ', args, type(args))

# soma_10 = soma(1,2,3,4,5,6,7,8,9,10)
# print(soma_10)

numeros = 1,2,3,4,5,6,7,8,9,10
# teste = soma(numeros) # dá erro, pois o *args vai empacotar uma tupla (numeros) como outra tupla
teste = soma(*numeros) # desempacotando numeros
print(teste)

"""
resumindo:
    *args - empacota
    *nome_da_variavel_iteravel = desempacota
"""
