def dm(a):
    return a * 2.54


def sm(a):
    return a / 2.54


def mili(a):
    return a * 1.61


def km(a):
    return a / 1.61


def funt(a):
    return a * 0.4536


def kg(a):
    return a / 0.4536


def unci(a):
    return a * 28.35


def gramm(a):
    return a / 28.35


def gallon(a):
    return a * 4.55


def litr(a):
    return a / 4.55


def pint(a):
    return a * 0.57


def litri(a):
    return a / 0.57


b = int(input('Input number '))
c = int(input('Input value '))
while b < 13:
    if b == 1:
        print(dm(c))
        b = int(input('Input number '))
    elif b == 2:
        print(sm(c))
        b = int(input('Input number '))
    elif b == 3:
        print(mili(c))
        b = int(input('Input number '))
    elif b == 4:
        print(km(c))
        b = int(input('Input number '))
    elif b == 5:
        print(funt(c))
        b = int(input('Input number '))
    elif b == 6:
        print(kg(c))
        b = int(input('Input number '))
    elif b == 7:
        print(unci(c))
        b = int(input('Input number '))
    elif b == 8:
        print(gramm(c))
        b = int(input('Input number '))
    elif b == 9:
        print(gallon(c))
        b = int(input('Input number '))
    elif b == 10:
        print(litr(c))
        b = int(input('Input number '))
    elif b == 11:
        print(pint(c))
        b = int(input('Input number '))
    elif b == 12:
        print(litri(c))
        b = int(input('Input number '))
    else:
        break