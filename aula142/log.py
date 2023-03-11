# Abstração
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    # template method = método que não está implementado
    def _log(self, msg):
        # nesse caso, colocamos o raise pra pessoa que for usar esse código
        # não usar a SUPER classe, e sim a SUB classe
        raise NotImplementedError('Implemente o método log')
    
    # o método é definido nas subclasses
    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
# LogFileMixin é um log
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log...', msg_formatada)
        with open(LOG_FILE, 'a', encoding='utf8') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Qualquer coisa')
    lp.log_success('Sucesso!')
    
    lf = LogFileMixin()
    lf.log_error('Qualquer coisa')
    lf.log_success('Sucesso!')

    # print(LOG_FILE)
