def decorator(fn):
    import time
    def wrapped(a, b):
        t = time.perf_counter()
        res = fn(a, b)
        print(a, b, time.perf_counter() - t)
        return res
    return wrapped

@decorator
def foo(a, b ):
    return a * b

b = foo(3, 5)

a = {'sdfsadf'}
print(list((map(lambda a: a[0] == 'c', a))))

a = '3'
print(list(map(lambda x: a.isdigit(), a)))

chisla = [13, 16, 19, 21, 25, 26]
print(list(filter(lambda x: x%13 == 0 or x%19 == 0, chisla)))




