# dir, hasattr, getattr
string = 'João'
metodo = 'upper'

if hasattr(string, metodo):
    print('(y)')
    print(getattr(string, metodo)())
else:
    print('fail..')
