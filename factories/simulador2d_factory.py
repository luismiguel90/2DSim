from models.simulador2d import (
    Simulador2DMapa1,
    Simulador2DMapa2,
    Simulador2DMapa3
)


class Simulador2DFactory:
    # Factory Method -> Decide qual o simulador concreto a criar (com base na configuração)

    @staticmethod
    def criar(activity_id, student_id, config):
        mapa = config.get("map_selection", "mapa_1")

        if mapa == "mapa_1":
            return Simulador2DMapa1(activity_id, student_id, config)
        elif mapa == "mapa_2":
            return Simulador2DMapa2(activity_id, student_id, config)
        elif mapa == "mapa_3":
            return Simulador2DMapa3(activity_id, student_id, config)
        else:
            raise ValueError("Mapa desconhecido!")
