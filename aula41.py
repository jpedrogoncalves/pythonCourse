"""
iterável => str, range, etc (__iter__)
iterador => quem sabe entregar um valor por vez
next => me entregue seu próximo valor
iter => me entregue seu iterador
"""
# texto = iter('João') # __iter__()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
texto = 'João'
iterator = iter(texto)
