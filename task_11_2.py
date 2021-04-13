class Car:
    def __init__(self, marka, model, speed=0):
        self.__marka = marka
        self.__model = model
        self.__speed = speed

    def zoom_in_speed(self):
        self.__speed += 5
        return self.__speed

    def decrease_speed(self):
        self.__speed -= 5
        return self.__speed
    def stop_spedd(self):
        self.__speed = 0
        return self.__speed
    def now_speed(self):
        print(self.__speed)

    def razvorot(self):
        self.__speed = -self.__speed
        return self.__speed

h1 = Car('bmw', 'x7')

h1.zoom_in_speed()
h1.now_speed()
h1.zoom_in_speed()
h1.now_speed()
h1.zoom_in_speed()
h1.now_speed()
h1.razvorot()
h1.now_speed()
h1.decrease_speed()
h1.now_speed()
h1.stop_spedd()
h1.now_speed()
h1.razvorot()
h1.now_speed()

