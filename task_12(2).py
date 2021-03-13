class ListIterator:
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 2
        return self._collection[self._cursor] ** 2

class ListCollection:
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection, -2)


_iterable = ListCollection([1, 2, 3, 4, 5, 6, 7])
for i in _iterable:
    print(i)
_iter = iter(_iterable)





