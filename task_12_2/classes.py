class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, x, y, dl_radius):
        self.point = Point(x=x, y=y)
        self.dl_radius = dl_radius

    def perimetr(self):
        p = self.dl_radius * 3.14 * 2
        return p

    def ploshad(self):
        s = (self.dl_radius ** 2) * 3.14
        return s


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        p = self.a + self.b + self.c
        return p

    def ploshad(self):
        s = (self.a + self.b) / 2
        return s


class Square(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        p = self.a * 2
        return p

    def ploshad(self):
        s = self.a * 4
        return s


def res():
    circle = Circle(1, 2, 3)
    triangle = Triangle(6, 4, 5)
    square = Square(7, 8)
    spis_figure = []
    spis_figure.append(circle.perimetr())
    spis_figure.append(circle.ploshad())
    spis_figure.append(triangle.perimetr())
    spis_figure.append(triangle.ploshad())
    spis_figure.append(square.perimetr())
    spis_figure.append(square.ploshad())
    return spis_figure
