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
    
    def incrementarIntensidade(self):
        self.intensidade = self.intensidade + 1
        print("O brilho atual é {}%!".format(self.intensidade))
        return self.intensidade


# Comando complexo

class ComandoComplexo(Comando):

    def __init__(self, receiver: LampadaSmart) -> None:
        self.receiver = receiver

    def execute(self) -> None:
        self.receiver.ligar()

# Invoker class
class InterruptorSmart:
    __button1_pressed = None
    
    def set_button1(self, command: Comando):
        self.__button1_pressed = command
    
    def pressed(self):

        if isinstance(self.__button1_pressed, Comando):
            self.__button1_pressed.execute()


if __name__ == "__main__":

    Lampada = LampadaSmart()
    Interruptor = InterruptorSmart()
    Interruptor.set_button1(ComandoComplexo(Lampada))

    Interruptor.pressed()

