# higher order functions - funções de primeira classe

# higher order functions = Funções que podem receber e/ou retornar outras funções
# first class functions = Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

# ambas podem ser diferentes, e ter o mesmo significado

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'bom dia', 'joão'))
print(executa(saudacao, 'boa noite', 'camila'))
