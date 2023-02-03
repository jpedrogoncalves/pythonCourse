# raise - lançando exceções (errors)
# print(123)
# raise ValueError('Deu erro!') # levanta o erro que você escolheu.
# print(456)

# def divide(n, d):
#     # código redundante, pois o erro seria mostrado normalmente
#     try:
#         return n / d
#     except ZeroDivisionError:
#         print('_______')
#         raise
def check_d_is_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por 0') # criando o próprio erro.
    return True

def verifica_tipo(n):
    type_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float \n' f'{type_n} enviado')
    if not isinstance(n, (float, int)):
        raise TypeError(f'{n} deve ser int ou float \n' f'{type_n} enviado')


def divide(n, d):
    verifica_tipo(n)
    verifica_tipo(d)
    check_d_is_zero(d)
    return n / d

print(divide('9', '2'))
