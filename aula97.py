# Módulos padrões do python (import, from, as e *)
# inteiro: import nome_modulo
# vantagens: você o tem o namespace do módulo
# desvantagens: nomes grandes

import sys
print(sys.platform)

# partes - from modulo import obj1, obj2
# vantagens: nomes curtos
# desvantagens: sem o namespace do módulo
# tomar cuidado pra não sobrescrever os nomes das funções.

from sys import platform, exit
print('bla')
print(platform)
# exit()

# alias1 - import nome_modulo as apelido
# alias2 - from nome_modulo import obj as apelido
# vantagens: você pode reservar nomes para seu código
# desvantagens: pode ficar fora do padrão da linguagem.

import sys as s
print(s.platform)

from sys import platform as pf, exit as ex
print(pf)
# ex()
print(213)

# má prática: from nome_modulo import *
# vantagens: importa tudo de um módulo
# desvantagens: importa tudo de um módulo
