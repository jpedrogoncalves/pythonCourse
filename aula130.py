# @staticmethod (método estático) são inúteis em Python
# métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self, nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.
class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi', args, kwargs)

c1 = Classe
c1.funcao_que_esta_na_classe(1,1,2,2,3,23)
Classe.funcao_que_esta_na_classe(name='Jop', age=25)
