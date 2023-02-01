# Generator expression, iterables e iterators em python

# iterable = tem responsabilidade de ter os valores sequencialmente
# iterator = entregar um valor por vez / saber qual o próximo valor.
import sys

iterable = ['Eu', 'tenho', '__iter__']
# iterator = iterable.__iter__()
iterator = iter(iterable)

# se o objeto tem __iter__, é um iterável

# print(next(iterator))

# generator: são funções que sabem pausar.
# generator não tem índices, nem tamanho, nem nada do que a lista tem
# todo generator é um iterator
# um iterator não é um generator

# isso gera problema, pois salva todos os dados na memória.
lista = [n for n in range(100000)]
generator = (n for n in range(100000)) # criando um generator <genexpr>
# pra ver o tamanho da lista na memória:
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
# o tamanho da lista sempre aumenta, mas o do generator continua o mesmo
# pois a lista salva todos os valores na memória e o generator não.

for n in generator:
    print(n)
