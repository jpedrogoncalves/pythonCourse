# precedencia dos operadores
# 1. (n+n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5 # 7
conta_2 = (1 + 1) ** (5 + 5) # 1024
print(conta_1)
print(conta_2)
