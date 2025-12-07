from factories.simulador2d_factory import Simulador2DFactory




class ActivityFactory:
    # Fábrica principal -> Uso do padrão Factory Method para criar simuladores 2D com diferentes variantes.

    @staticmethod
    def criar_2d_simulator(activity_id, student_id, config):
        return Simulador2DFactory.criar(activity_id, student_id, config)