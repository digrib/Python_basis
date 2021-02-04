#--------------------------2--------------------------------#

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc(self):
        print(f"Масса асфальта - {self._length * self._width * 25 * 5 / 1000} тонн")

def main():
    while True:
        try:
            road_a = Road(int(input("Ширина дороги в м: ")), int(input("Длина дороги в м: ")))
            road_a.calc()
            break
        except ValueError:
            print("Только числа!")

#-----------------------------------3-----------------------#

class Work:
    def __init__(self, name, s_name, pos, wag, bon):
        self.name = name
        self.s_name = s_name
        self.pos = pos
        self._inc = {"profit": wag, "bonus": bon}

class Pos(Work):
    def full_name(self):
        return f"{self.name} {self.s_name}"

    def full_prof(self):
        return f"{sum(self._inc.values())}"

manager = Pos("Dim", "Grib", "PhD", 100000, 150000)
print(manager.full_name())
print(manager.pos)
print(manager.full_prof())

#----------------------------4-------------------------#

class Car:

    def __init__(self, name, color, speed, police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.police = police
        print(f"New car - {self.name} with color - {self.color}. Police car - {self.police}")

    def go(self):
        print(f"{self.name} is driven.")

    def stop(self):
        print(f"{self.name} stopped")

    def turn(self, dir_):
        print(f"{self.name} turned {'left' if dir_ == 0 else 'right'}.")

    def s_speed(self):
        return f"{self.name}: speed: {self.speed}"

class TCar(Car):
    def s_speed(self):
        return f"{self.name}: speed: {self.speed} Speed exceeded!" \
                if self.speed > 60 else f"{self.name} has speed - {self.speed}"

class WCar(Car):
    def s_speed(self):
        return f"{self.name}: speed: {self.speed} Speed exceeded!" \
                if self.speed > 40 else f"{self.name} has speed - {self.speed}"

class SportCar(Car):
    def s_speed(self):
        return f"{self.name}: speed: {self.speed}"

class PoliceCar(Car):
    def __init__(self, name, color, speed, police=True):
        super().__init__(name, color, speed, police)

police_car = PoliceCar("автозак", "хаки", 60)
police_car.go()
print(police_car.s_speed())
police_car.turn(0)
police_car.stop()
print()

sport_car = SportCar("Ferrari", "red", 210)
sport_car.go()
sport_car.turn(1)
print(sport_car.s_speed())
sport_car.stop()
print()

w_car = WCar("Gazel", "желтый", 60)
w_car.go()
w_car.turn(0)
print(w_car.s_speed())
w_car.turn(1)
w_car.stop()
print()

t_car = TCar("Volga", "black", 40)
t_car.go()
t_car.turn(1)
t_car.stop()
t_car.go()
t_car.turn(0)
print(t_car.s_speed())
t_car.stop()

print(f"\n Car {t_car.name} {t_car.color}")
print(f"Police car {police_car.name} {police_car.color}")

#---------------------------------5-------------------------#

class Stationery:
    def __init__(self, title="drawing smth"):
        self.title = title

    def draw(self):
        print(f"{self.title} just drew")

class Pen(Stationery):
    def draw(self):
        print(f"I've  just drew with {self.title} pen")

class Pencil(Stationery):
    def draw(self):
        print(f"I've just drew with {self.title} pencil")

class Marker(Stationery):
    def draw(self):
        print(f"I've just drew with {self.title} marker")

abb = Stationery()
abb.draw()
pen = Pen("Gloria")
pen.draw()
pencil = Pencil("Dash")
pencil.draw()
marker = Marker("Komus")
marker.draw()

#--------------------------------10------------------------#


import time
import itertools

class TL:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [10, 32], ["yellow", [2, 33]]]]


    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])

TL_1 = TL()
TL_1.running()

