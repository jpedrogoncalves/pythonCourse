# yield from
def gen1():
    print('g1')
    yield 1
    yield 2
    yield 3
    print('end g1')

def gen3():
    print('g3')
    yield 10
    yield 20
    yield 30
    print('end g3')

def gen2(gen):
    print('g2')
    yield from gen()
    yield 4
    yield 5
    yield 6
    print('end g2')

g1 = gen2(gen1)
g2 = gen2(gen3)
for numero in g1:
    print(numero)
for numero in g2:
    print(numero)
