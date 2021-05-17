import time
import threading
import multiprocessing

import requests
from bs4 import BeautifulSoup


def foo():
    url = 'https://tut.by/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div')
    return items


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


def pool():
    a = time.perf_counter()
    t1 = multiprocessing.Pool(processes=2)
    t1.apply_async(foo)
    t1.apply_async(foo)
    t1.close()
    t1.join()
    b = time.perf_counter() - a
    print(b)


if __name__ == '__main__':
    time_foo()
    potoki()
    pool()
#каждый раз по разному выдает время работы, в зависимости от количетсва запросов на сайт
#но по правильному при параллельном запросе I/O должен работать быстрей, чем последовательно