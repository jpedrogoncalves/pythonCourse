import importlib

import aula99_m

print(aula99_m.variavel)

for i in range(10):
    # singleton: só pode existir uma única instância enquanto o programa estiver executando.
    # o python salva o módulo na memória.
    # o módulo só é recarregado se você solicitar.
    importlib.reload(aula99_m)
    print(i)
