"""
Cálculo do segundo dígito
CPF: 746.824.890-70
Colete a soma dos primeiros 9 dígitos do CPF,
MAIS O PRIMEIRO DÍGITO
multiplicando cada um dos valores por uma 
contagem regressiva começando de 11

Ex: 
    746.824.890-70 (746824890)
    10 9  8  7  6  5  4  3  2
    7  4  6  8  2  4  8  9  0
    70 36 48 56 12 20 32 27 0

    Somar todos os resultados: 301
    Multiplicar o resultado por 10: 3010
    Obter o resto da divisão por 11: 3010%11 = 7

    Se o resultado da divisão for maior que 9:
        result = 0
    contrário disso:
        resultado é o valor da conta

O primeiro dígito do cpf é 7
"""
cpf_enviado_usuario = '36440847007'
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')
