# # main
# from sys import path

# import aula100_package.modulo # usa o nome todo como namespace
# # from aula100_package.modulo import soma_modulo
# from aula100_package.modulo import * # má prática.
# from aula100_package import modulo

# print(variavel)
# print(nova)
# # print(soma_modulo(1,2))

# # print(*path, sep='\n')

# o erro ocorre, porque na importação de soma_modulo
# está no 'escopo' de aula100_package
# e na hora que o código é executado fora do escopo, não há
# nenhum arquivo com o nome modulo_b ou modulo

# from aula100_package.modulo import soma_modulo
# soma_modulo()

#__init__ é executado assim que o módulo é importado.

import aula100_package
print(aula100_package.soma_modulo(2,3))
