from abc import ABC, abstractmethod

class SimuladorBase(ABC):
    '''
        Subjeto abstrato para o o padrão Proxy
        Define a interface entre Proxy e o simulador real
    '''

    def __init__(self, activity_id, student_id, config):
        self.activity_id = activity_id
        self.student_id = student_id
        self.config = config
        self.analytics = {}

    @abstractmethod
    def iniciar(self):
        pass