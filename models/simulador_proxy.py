from models.simulador_base import SimuladorBase


class SimuladorProxy(SimuladorBase):
    '''
        Proxy do Sim2D. Controla o acesso ao simulador real (encapsula-o e implmenta a mesma interface).
    '''

    def __init__(self, simulador_real):
        super().__init__(simulador_real.activity_id, simulador_real.student_id, simulador_real.config)
        
        self._simulador_real = simulador_real

    
    def iniciar(self):
        '''
        Por enquanto delega.

        A fazer:
            -> Lógica de controlo como por exemplo: 
                    -validação de sessão
                    -limite de tentativas
                    -logging
                    -permissões
        '''
        return self._simulador_real.iniciar()