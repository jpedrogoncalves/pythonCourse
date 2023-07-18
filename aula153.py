# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe calable.
class CallMe:
    def __init__(self, phone):
        self.phone = phone

    # ? faz a instância da classe ser executável.
    def __call__(self, nome):
        # * podemos fazer qualquer coisa
        print(nome, 'está CHAMANDO,', self.phone)
        return 123124

# ! chamando a CLASSE
call1 = CallMe('128937')
# ! chamando a INSTÂNCIA
retorno = call1('Luiz otavio')
print(retorno)
