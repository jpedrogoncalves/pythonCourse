# try / except
# int('a') # aqui levanta a exceção! (ValueError)
numero_str = input('Insira o número: ')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

try:
    print('STR: ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_str)
    print(f'O dobro de numero_str é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
