# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final (convenção))
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
    # podemos mandar várias coisas no erro:
    exception_ = MyError('a', 'b', 'c')
    # e chega no error em args
    raise exception_

# traceback = caminho até o erro

# tratando o erro
try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    """
        nesse caso, não temos como saber o nome do erro
        porque estamos tratando de duas classes.
        para saber o nome da classe, podemos usar:
    """
    print(error.__class__.__name__)
    print(error)

    exception_ = OutroError('vou lançar de novo')

# relançando a exceção:
    raise exception_ from error
