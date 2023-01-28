# exercício - sistema de perguntas e respostas
perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '2', '3', '4'],
        'Resposta' : '4'
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['10', '24', '25', '0'],
        'Resposta' : '25'
    },
    {
        'Pergunta' : 'Quanto é 12+12?',
        'Opções' : ['12', '0', '24', '1212'],
        'Resposta' : '24'
    },
    {
        'Pergunta' : 'Quanto é 18*8?',
        'Opções' : ['144', '188', '354', '420'],
        'Resposta' : '144'
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha_int = None
    acertou = False
    qtd_opcoes = len(opcoes)
    escolha = input('Escolha uma opção: ')

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou! 🥳')
    else:
        print('Errou! 😪')

    print()

print(f'Você acertou: {qtd_acertos} opções!')
