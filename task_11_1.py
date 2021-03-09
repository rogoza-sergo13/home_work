class Cat:
    def __init__(self, color, age, poroda, rost):
        self.__color = color
        self.__age = age
        self.__poroda = poroda
        self.rost = rost

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run!')


class Car:
    def __init__(self, marka, kyzov, god_vipyska, kolesa):
        self.__model = marka
        self.__kyzov = kyzov
        self.__god_vipyska = god_vipyska
        self.kolesa = kolesa

    def speed(self):
        print('Sporting car')

    def jeep(self):
        print('Big fut')


class People:
    def __init__(self, height, kg, pol, rassa):
        self.__height = height
        self.__kg = kg
        self.__pol = pol
        self.rassa = rassa

    def nationalnost(self):
        print(self.rassa)

    def telo(self):
        if self.__kg < 50:
            print('Hudoi')


class Mobile:
    def __init__(self, memory, size, model):
        self.__memory = memory
        self.__size = size
        self.__model = model

    def music(self):
        print('Cool music')

    def camera(self):
        print('Good video')


class House:
    def __init__(self, material, komnati, dlina, shirina):
        self.__material = material
        self.__komnati = komnati
        self.__dlina = dlina
        self.shirina = shirina

    def room(self):
        if self.__komnati > 6:
            print('Big house')

    def area(self):
        return self.__dlina * self.shirina


h1 = House(1, 7, 3, 4)
print(h1.room())
