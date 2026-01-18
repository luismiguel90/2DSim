from models.simulador_base import SimuladorBase


# Objetos que o aluno nunca vai aceder diretamente


class Simulador2DMapa1(SimuladorBase):
    def __init__(self, activity_id, student_id, config):
        super().__init__(activity_id, student_id, config)
        self.x = 0
        self.y = 0
        self.carrying = False
        self.commands = []

    def iniciar(self):
        return "Simulador 2D -> Mapa 1 iniciado."
    
    def adicionar_comando(self, command):
        self.commands.append(command)

    def executar_comandos(self):
        resultados = []
        for command in self.commands:
            resultados.append(command.execute(self))
        self.commands.clear()           # Limpar a lista para evitar repeticoes anteriores
        return resultados
    
class Simulador2DMapa2(Simulador2DMapa1):
    def iniciar(self):
        return "Simulador 2D -> Mapa 2 iniciado."
    
class Simulador2DMapa3(Simulador2DMapa1):
    def iniciar(self):
        return "Simulador 2D -> Mapa 3 iniciado."
    