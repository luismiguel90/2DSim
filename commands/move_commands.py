from commands.command_base import Command

'''
    Comandos de movimento
'''

class MoveUp(Command):
    def execute(self, simulador):
        simulador.y -= 1
        return "Para cima"
    
class MoveDown(Command):
    def execute(self, simulador):
        simulador.y += 1
        return "Para baixo"
    
class MoveLeft(Command):
    def execute(self, simulador):
        simulador.x -= 1
        return "Para esquerda"
    
class MoveRight(Command):
    def execute(self, simulador):
        simulador.x += 1
        return "Para direita"
    