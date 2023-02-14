# count é um iterador sem fim
from itertools import count

# inicia do 10 até o infinito
c1 = count(8, 8) # iterator infinito
r1 = range(8, 100, 8)

# provando que é um iterator
print('c1', hasattr(c1, '__iter__')) 
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__')) 
print('r1', hasattr(r1, '__next__'))

print('count: ')
for i in c1:
    if i >= 100:
        break

    print(i)

print()

print('range: ')
for i in r1:
    print(i)
