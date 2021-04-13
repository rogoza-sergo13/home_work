import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def get_length(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


class Figure:
    pass


class Circle(Figure):
    def __init__(self, center, dl_radius):
        self.center = center
        self.dl_radius = dl_radius

    def perimetr(self):
        return self.dl_radius * math.pi * 2

    def ploshad(self):
        return (self.dl_radius ** 2) * math.pi


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return get_length(self.b, self.a) + get_length(self.c, self.b) + get_length(self.c, self.a)

    def ploshad(self):
        p1 = get_length(self.b, self.a)
        p2 = get_length(self.c, self.b)
        p3 = get_length(self.c, self.a)
        p = (p1 + p2 + p3) / 2
        return math.sqrt(p * (p - p1) * (p - p2) * (p - p3))


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        return get_length(self.b, self.a) * 4

    def ploshad(self):
        return get_length(self.b, self.a) ** 2 / 16
