# entendendo módulos em python
# o primeiro módulo se chama __main__
# você pode importar outro módulo interno ou parte do módulo
# o python conhece a pasta onde o __main__ está e as pastas abaixo
# dele
# ele não reconhece pastas e módulos acima por padrão
# o python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

import aula98_m
from aula98_m import variavel_mod

# main é o start do programa

# print('esse módulo se chama: ', __name__)
# print(*sys.path, sep='\n')
print(aula98_m.variavel_mod)
print(variavel_mod)
