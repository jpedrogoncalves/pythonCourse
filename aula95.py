# try, except, else, finally

# try + else não funciona
# try:
#     a = 10
#     b = 0
#     print('l1'[920832])
#     print(b[9])
#     c = a / b # má prática, pois o erro está silenciado
#     print('l2') # não é mostrada, pois o try pula de onde o erro ocorreu
# except ZeroDivisionError:
#     print('dividiu por zero.')
# except NameError:
#     print('nome b não está definido')
# except (TypeError, IndexError) as error: # caso você queira saber qual exceção ocorreu, divide em duas.
#     print('Type error + IndexError')
#     print(f'msg: {error}')
#     print(f'nome: {error.__class__.__name__}')
# except Exception:
#     print('?')

# print('Cont.')

# FINALLY:
try:
    print('try')
    # 8/0
except ZeroDivisionError:
    print('divisão por 0')
else:
    # else no try, é executado quando o código funciona sem erros.
    print('Não ocorreu erro.')
finally:
    # sempre será executado, mesmo que ocorra um erro.
    print('finally')

