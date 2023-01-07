# calculadora com while.
while True:
    user_number1_input = input('Insira o primeiro número: ')
    user_number2_input = input('Insira o segundo número: ')
    input_operator = input('Insira o operador (+ - / *): ')

    valid_numbers = None
    valid_operators = '+-/*'
    number1_float = 0
    number2_float = 0

    try:
        number1_float = float(user_number1_input)
        number2_float = float(user_number2_input)
        valid_numbers = None
    except:
        valid_numbers = True

    if valid_numbers:
        print('Um, ou ambos os números são inválidos.')
        continue

    if input_operator not in valid_operators:
        print('Operador inválido!')
        continue

    if len(input_operator) > 1:
        print('Mais de um operador selecionado, tente novamente!')
        continue

    print('Confira o resultado da sua conta abaixo: ')
    if input_operator == '+':
        print(number1_float + number2_float)
    elif input_operator == '-':
        print(number1_float - number2_float)
    elif input_operator == '/':
        print(number1_float / number2_float)
    elif input_operator == '*':
        print(number1_float * number2_float)
    else:
        print('Ops! Algo de errado ocorreu!')
        continue

    logout = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if logout:
        break

