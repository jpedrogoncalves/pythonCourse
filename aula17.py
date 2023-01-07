primeiro_valor = input('insira o primeiro numero: ')
segundo_valor = input('insira o segundo numero: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual do que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior ou igual do que {primeiro_valor=}')
else:
    ...