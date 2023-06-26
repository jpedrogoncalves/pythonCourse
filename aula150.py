# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

# ? na real, não é uma função e sim um GENERATOR
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu o erro: ', e)
    finally:
        print('fechando arquivo')
        arquivo.close()

with my_open('aula150.txt', 'w') as arquivo:
    # * arquivo tem o retorno de __enter__
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
