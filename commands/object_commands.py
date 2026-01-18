from commands.command_base import Command

'''
    Comando de interação com objetos
'''

class PickObject(Command):
    def execute(self, simulador):
        simulador.carrying = True
        return "Objeto apanhado"
    
class DropObject(Command):
    def execute(self, simulador):
        simulador.carrying = False
        return "Objeto largado"
    