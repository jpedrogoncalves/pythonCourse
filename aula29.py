"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

user_number_input = input('Insira o número: ')
if user_number_input.isdigit():
    user_number_input = int(user_number_input)
    if user_number_input % 2 == 0:
        print(f'O número {user_number_input} é par')
    else:
        print(f'O número {user_number_input} é ímpar')
else:
    print('Não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia: 0~11 / Boa tarde: 12~17 / Boa noite: 18 ~ 23
"""

# print('Bom dia: 0~11 / Boa tarde: 12~17 / Boa noite: 18 ~ 23')
# user_hour_input = input('Insira a hora: ')
# if user_hour_input.isdigit():
#     user_hour_input = int(user_hour_input)
#     dia = user_hour_input >= 0 and user_hour_input <= 11
#     tarde = user_hour_input >= 12 and user_hour_input <= 17
#     noite = user_hour_input >= 18 and user_hour_input <= 23
#     if dia:
#         print('Bom dia!')
#     elif tarde:
#         print('Boa tarde!')
#     elif noite:
#         print('Boa noite!')
#     else:
#         print('Por favor, insira a hora corretamente!')
# else:
#     print('Por favor, insira a hora corretamente!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 ou 
menos, escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva "seu nome
é normal"; maior que 6, escreva "seu nome é muito grande".
"""
user_name_input = input('Insira o seu nome: ')
len_name = len(user_name_input)
print(len_name)
if len_name <= 4:
    print('Seu nome é curto.')
elif len_name >= 5 and len_name <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
