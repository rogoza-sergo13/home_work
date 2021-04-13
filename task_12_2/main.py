from classes import Circle, Triangle, Square, Point

def res():
    circle = Circle(1, 2)
    triangle = Triangle(Point(0, 1), Point(2, 3), Point(10, 2))
    square = Square(Point(0, 1), Point(4, 4))
    spis_figure = []
    spis_figure.append(circle.ploshad())
    spis_figure.append(triangle.ploshad())
    spis_figure.append(square.ploshad())
    return spis_figure
print(res())