# closure e funções que retornam outras funções
def criar_saudacao(saudacao):
    # o python salva os parametros de criar_saudacao pra resolver a execução de 
    # saudar, antes de executar criar_saudacao()
    
    # ao passar nome para saudar, deixamos a saudação estática
    # e o nome dinâmico
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    # return saudar() # função que executa antes da hora
    # queremos adiar a execução da função
    return saudar # retorna a função, e não executa

falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('boa noite')

print(falar_bom_dia('joão')) # aponta para as funções que estão na memória / closure acontece aqui, quando executamos saudar
print(falar_boa_noite('camila')) # aponta para as funções que estão na memória / closure acontece aqui, quando executamos saudar

# exemplos de utilização:
nomes = ['Alice', 'Artur', 'Miguel', 'João', 'Laura', 'Camila']

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
