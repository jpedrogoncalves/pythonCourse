# valores padrão para parâmetros
# refatorar: editar o código

def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

# def multiplica(x, y=None, z=None): = Após nomear valor padrão, todos após tem que ser nomeados também.
#     return x * y
        

soma(1, 2)
soma(3, 2)
soma(1, 7)
soma(10, 9, 20)
