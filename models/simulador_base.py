from abc import ABC, abstractmethod

class SimuladorBase(ABC):
    '''
        Classe base abstrata para simuladores 2D

    '''

    def __init__(self, activity_id, student_id, config):
        self.activity_id = activity_id
        self.student_id = student_id
        self.config = config
        self.analytics = {}

    @abstractmethod
    def iniciar(self):
        pass