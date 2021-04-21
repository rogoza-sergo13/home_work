class Car:
    def __init__(self, marka, model, speed=0):
        self.__marka = marka
        self.__model = model
        self.__speed = speed

    def zoom_in_speed(self):
        self.__speed += 5
        return self.__speed

    def decrease_speed(self):
        if self.__speed < 5:
            print("Your speed is not really, step on the gas")
        else:
            self.__speed -= 5
        return self.__speed

    def stop_spedd(self):
        try:
            if self.__speed == 0:
                raise ValueError
        except ValueError:
            print("We've stopped, it's time to move")
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
h1.decrease_speed()
h1.now_speed()
h1.razvorot()
h1.now_speed()
h1.decrease_speed()
h1.now_speed()
h1.zoom_in_speed()
h1.now_speed()
h1.decrease_speed()
h1.now_speed()
h1.stop_spedd()
