f = open("123.txt", "r")
def foo(file_name):
    for line in f:
        yield line.strip()

print(next(foo('123.txt')))
print(next(foo('123.txt')))
print(next(foo('123.txt')))
print(next(foo('123.txt')))



