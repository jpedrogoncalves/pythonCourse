"""
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
"""
def criar_multiplicador(multiplicador): # por quanto o NÚMERO vai ser multiplicado
    def multiplicar(numero): # multiplica o número pelo MULTIPLICADOR
        return numero * multiplicador
    return multiplicar # retorna a função sem executar

duplicar = criar_multiplicador(2) # criamos o multiplicador 2
triplicar = criar_multiplicador(3) # criamos o multiplicador 3
quadruplicar = criar_multiplicador(4) # criamos o multiplicador 4

print(duplicar(2)) # finalizamos a execução de multiplicar, passando o numero 2
print(triplicar(2))
print(quadruplicar(2))
