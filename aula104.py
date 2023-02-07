# funções decoradoras e decoradores
# decorar = adicionar / remover / restringir / alterar
# funções decoradoras são funções que decoram outras funções.
# decoradores são usados para fazer o python
# usar as funções decoradoras em outras funções.
# decoradores são "Syntax Sugar" (açúcar sintático)

# função decoradora
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('decorar')
        for arg in args:
            is_string(arg)
        
        resultado = func(*args, **kwargs)
        print('decorada')
        return resultado
    return interna

@criar_funcao # syntax sugar
# quero que use a 'criar_funcao' na função inverte_string
def inverte_string(string):
    # o python troca inverte_string para interna (nome da função do closure)
    print(f'Nome da função, pós @criar_funcao: {inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# inverte_string_checando_parametros = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametros('123')

invertida = inverte_string('123')
print(invertida)
