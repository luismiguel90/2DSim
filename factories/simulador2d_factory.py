from models.simulador2d import(Simulador2DMapa1,Simulador2DMapa2,Simulador2DMapa3)
from models.simulador_proxy import SimuladorProxy



class Simulador2DFactory:
    # Factory Method -> Decide qual o simulador concreto a criar (com base na configuração) e devolve um Proxy.

    @staticmethod
    def criar(activity_id, student_id, config):
        mapa = config.get("map_selection","mapa_1")

        if mapa == "mapa_1":
            simulador_real = Simulador2DMapa1(activity_id, student_id, config)
        elif mapa == "mapa_2":
            simulador_real = Simulador2DMapa2(activity_id, student_id, config)
        elif mapa == "mapa_3":
            simulador_real = Simulador2DMapa3(activity_id, student_id, config)
        else:
            raise ValueError(("Mapa desconhecido!"))
        
        # Retorna o Proxy que controla o acesso ao simulador real
        # app.py  não interage diretamente com o Simulador2D do mapa concreto
        return SimuladorProxy(simulador_real)