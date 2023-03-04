# @property + @setter - getter e setter no modo pythônico
# getter -> obter valor
#   -como getter
#   -p/ evitar quebrar código cliente
#   -p/ habilitar setter
#   -p/ executar ações ao obter um atributo
class Caneta:
    def __init__(self, cor):
        # esse cor (começa com _) (abaixo) NÃO DEVE SER USADO FORA DA CLASSE!!!!!
        self._cor = cor
        self._cor_tampa = None
        # para executar o setter já no init:
        # self.cor = cor

    @property
    def cor(self):
        # print('PROPERTY')
        return self._cor
    
    @cor.setter
    # é um método que tem o self, e tem que receber um valor
    def cor(self, valor):
        # print(valor)
        # if valor == 'rosa':
            # raise ValueError('Não aceito!')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

caneta = Caneta('Azul')
print(caneta.cor)
caneta.cor = 'VERMELHO!'
print(caneta.cor)
print(caneta.cor_tampa)
caneta.cor_tampa = 'Azul!'
print(caneta.cor_tampa)
