# Logic operators
# or

# se qualquer valor for considerado verdadeiro
# a expressão inteira será considerada verdadeira

# entrada = input('[E]ntrar [S]air: ')
# usenha = input('Senha: ')
# senha = '123456'

# if (entrada == 'E' or entrada == 'e') and usenha == senha:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True or False)
print(True or False or 0 or 'abc' or True)
senha = input('Digite sua senha') or 'Sem senha'
print(senha)
