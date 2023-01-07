# introdução ao desenpacotamento
nomes = ['Maria', 'João', 'Camila']
nome1, nome2, nome3 = nomes
#nome1, nome2 = nomes -> ValueError: too many values to unpack
#nome1, nome2, nome3, nome4 = nomes -> ValueError: not enough values to unpack

#problema: pegar só o primeiro valor de nomes. SOLUÇÃO:
nome, *_ = nomes
# o _, pode ser usado antes e depois

print(nome, _)
