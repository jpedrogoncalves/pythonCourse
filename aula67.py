"""
escopo de funções em python
escopo significa o local onde aquele código pode atingir.
existe o escopo global e local
global - onde todo o código é alcançavel 
local - apenas nomes do mesmo local podem ser alcançados
não temos acesso a nomes do escopo interno nos escopos
externos.

a palavra 'global' faz uma variável do escopo externo
ser a mesma no e. interno.
"""
x = 1
def escopo():
    global x
    x = 10
    def escopo2():
        global x
        x = 2
        y = 3
        print(x, y)
    escopo2()
    print(x)

print(x)
escopo()
print(x)
