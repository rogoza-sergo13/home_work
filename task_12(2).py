class ListIterator:
    def __init__(self, collection, cursor=0):
        self._collection = collection
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor > len(self._collection):
            raise StopIteration()
        a = self._collection[self._cursor] ** 2
        self._cursor += 2
        return a


class ListCollection:
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return ListIterator(self._collection)


_iterable = ListCollection([1, 2, 3, 4, 5, 6, 7])
for i in _iterable:
    print(i)
_iter = iter(_iterable)
