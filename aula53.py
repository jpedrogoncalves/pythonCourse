# imprecisão de números flutuantes
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print(numero_3)
print(f'{numero_3:.2f}') # maneira de arredondar

# obs: se o final do numero for inteiramente 0, ele não exibe os 0.
print(round(numero_3, 1)) # round(numero, qtd_casas_decimais) 
