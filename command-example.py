from __future__ import annotations
from abc import ABC, abstractmethod

class Comando(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

# Receiver class
class LampadaSmart:
    def __init__(self) -> None:
        self.estado = False
        self.intensidade = 50

    def ligar(self):
        self.estado = True
        print("A lampada está ligada!")
        return self.estado
    
    def desligar(self):
        self.estado = False
        print("A lampada está desligada!")
        return self.estado
    
    def incrementarIntensidade(self):
        self.intensidade = self.intensidade + 1
        print("O brilho atual é {}%!".format(self.intensidade))
        return self.intensidade


# Comando complexo

class ligar(Comando):

    def __init__(self, receiver: LampadaSmart) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.ligar()

class desligar(Comando):

    def __init__(self, receiver: LampadaSmart) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.desligar()

# Invoker class
class InterruptorSmart:
    __button1_pressed = None
    __button1_against = None
    
    def set_button1_pressed(self, command: Comando):
        self.__button1_pressed = command
    
    def set_button2_against(self, command: Comando):
        self.__button1_against = command

    def pressed(self):

        if isinstance(self.__button1_pressed, Comando):
            self.__button1_pressed.execute()

    def against(self):

        if isinstance(self.__button1_against, Comando):
            self.__button1_against.execute()



if __name__ == "__main__":

    Lampada = LampadaSmart()
    Interruptor = InterruptorSmart()
    Interruptor.set_button1_pressed(ligar(Lampada))
    Interruptor.set_button2_against(desligar(Lampada))

    Interruptor.pressed()
    Interruptor.against()

