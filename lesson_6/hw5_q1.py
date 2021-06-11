from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color)
            sleep(sec)


tl = TrafficLight()
tl.running()
