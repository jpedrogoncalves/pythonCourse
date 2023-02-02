# introdução às generators functions
# generator = (n for n in range(100))

# def generator(n=0):
#     yield 1 # pausa a execução da função.
#     # return 'continua' # raise StopIteration, o return levanta uma exceção.
#     print('continua')
#     yield 2
#     print('mais uma')
#     yield 3
#     print('encerrando')
#     return 'over.'

# gen = generator(n=0)
# # iterator
# # print(iter(gen))
# for n in gen:
#     print(n)
def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return 'end.'


gen = generator(n=0)
for n in gen:
    print(n)
