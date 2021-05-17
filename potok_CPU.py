import time
import math
import threading
import multiprocessing


def foo():
    return math.factorial(100000)


def time_foo():
    a = time.perf_counter()
    foo()
    b = time.perf_counter() - a
    print(b)


def potoki():
    a = time.perf_counter()
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    b = time.perf_counter() - a
    print(b)


# два потока в одном процессе выполняются на одном ядре по времени в два раза больше потому что выполняются
# последовательно т.е. два раза одна и таже функция foo = 0.25 foo *2 = 0.46 (примерно)

def pool():
    a = time.perf_counter()
    t1 = multiprocessing.Pool(processes=2)
    t1.apply_async(foo)
    t1.apply_async(foo)
    t1.close()
    t1.join()
    b = time.perf_counter() - a
    print(b)


# два процесса выполняются на разных ядрах дольше, так как затрачивается время на переключение между процессами

if __name__ == '__main__':
    time_foo()
    potoki()
    pool()
