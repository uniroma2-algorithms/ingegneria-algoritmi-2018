"""
    File name: fibonacci.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Iterator dei numeri di Fibonacci
"""

from itertools import islice


class FibIter:
    """
    Iterator dei numeri di Fibonacci
    """
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value


class FibIterMax(FibIter):
    """
    Iterator di Fibonacci che si fermano al
    max-esimo numero
    """
    def __init__(self, max):
        super().__init__()
        self.max = max
        self.n = 0

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        self.n += 1
        if self.n > self.max:
            raise StopIteration  # ferma l'iterazione
        return value


if __name__ == "__main__":
    fib = FibIter()
    for _ in range(10):  # primi 10 numeri di fibonacci
        print(next(fib))

    limited = list(islice(fib, 0, 10))  # numeri di Fibonacci da 11 a 20 (l'iterator 'ricorda' l'ultimo numero ritornato
    print(limited)

    #for f in fib:    # sequenza infinita
    #    print(f)

    fibMax = FibIterMax(10)

    for i in fibMax:
        print(i)   # sequenza finita