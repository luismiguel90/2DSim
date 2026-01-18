from abc import ABC, abstractmethod

class Command(ABC):
    '''
        Base do padrão Command
        Classe base para os comandos do robot
    '''
    @abstractmethod
    def execute(self, simulador):
        pass