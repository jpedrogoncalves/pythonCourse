"""
CPF: 746.824.890-70
Colete a soma dos primeiros 9 dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

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
cpf = '47846765035'
nine_digits = cpf[:9]
regressive_counter = 10
conta = 0

for digit in nine_digits:
    resultado = int(digit) * regressive_counter
    regressive_counter -= 1
    conta += resultado

conta *= 10
conta %= 11

# variavel = 'Valor' if condicao else 'Outro valor'
resultado = conta if conta <= 9 else 0
print(resultado)
