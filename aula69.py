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
        print(i, total)
    print(total)
    # print('args: ', args, type(args))

soma(1,2,3,4,5,6,7,8,9,10)
