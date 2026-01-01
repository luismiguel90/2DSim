from models.simulador_base import SimuladorBase


# Objetos que o aluno nunca vai aceder diretamente


class Simulador2DMapa1(SimuladorBase):
    def iniciar(self):
        return "Simulador 2D -> Mapa 1 iniciado."
    
class Simulador2DMapa2(SimuladorBase):
    def iniciar(self):
        return "Simulador 2D -> Mapa 2 iniciado."
    
class Simulador2DMapa3(SimuladorBase):
    def iniciar(self):
        return "Simulador 2D -> Mapa 3 iniciado."
    