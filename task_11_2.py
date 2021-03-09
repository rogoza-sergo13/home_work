class Car:
    def __init__(self, marka, model, speed):
        self.__marka = marka
        self.__model = model
        self.__speed = speed

    def zoom_in_speed(self):
        speed1 = self.__speed + 5
        return speed1
    def decrease_speed(self):
        speed1 =  self.__speed - 5
        return speed1

    def stop_spedd(self):
        speed1 = self.__speed * 0
        return speed1
    def now_speed(self):
        speed1 = self.__speed
        return speed1

    def razvorot(self):
        speed1 = self.__speed - self.__speed * 2
        return speed1


h1 = Car('bmw', 'x7', 0)
print(h1.zoom_in_speed())
print(h1.decrease_speed())
print(h1.stop_spedd())
print(h1.now_speed())
print(h1.razvorot())
