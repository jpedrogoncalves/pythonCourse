"""
Formatação de strings
s- string
d- int
f- float
.<nº de dígitos>f
x ou X- hexadecimal
(Caractére)(><^)(quantidade)
>- esquerda
<- direita
^- centro
=- Força o nº a aparecer depois dos zeros
sinal = - ou +
Ex.: 0>-100, .1f

Conversion flags: !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:#>10}')
print(f'{variavel:-<10}')
print(f'{1000.423984724:0=+10,.1f}')
print(f'o hexadecimal de 1500 é: {1500:08X}')
# print(f'{variavel!r}')
