class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self):
        print('turn')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('speed exceeded')
        else: print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('speed exceeded')
        else:
            print(self.speed)


class PoliceCar(Car):
    pass


car_1 = WorkCar(42, 'red', 'Mitsu', False)
car_2 = PoliceCar(20, 'blue', 'Toyo', True)
car_3 = TownCar(59, "green", 'WV', False)
car_4 = SportCar(300, 'yellow', 'Porsche', False)
print(car_1.speed)
print(car_2.police)
print(car_3.color)
print(car_4.name)
car_3.stop()
car_1.turn()
car_4.go()
car_1.show_speed()
car_3.show_speed()