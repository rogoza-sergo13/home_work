def decoretor(func):
    def wrapper(a):
        a = list(filter(lambda x: int(x) % 2, a))
        return a
    return wrapper
a = input('Input number ')
@decoretor
def foo():
    return a
print(foo(a))