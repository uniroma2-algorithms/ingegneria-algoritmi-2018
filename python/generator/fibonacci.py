"""
    File name: fibonacci.py
    Author: Ovidiu Daniel Barba
    Date created: 10/12/2018
    Python Version: 3.7

    Generator dei numeri di Fibonacci
"""
from itertools import islice


def fibGen():
    """
    Generator dei numeri di Fibonacci. Rispetto all'iterator,
    è una funzione
    :return:
    """
    prev, curr = 0, 1
    while True:
        yield curr    # una funzione con yield è un generator
        prev, curr = curr, prev + curr


if __name__ == "__main__":
    fib = fibGen()

    for _ in range(10):  # primi 10 numeri di fibonacci
        print(next(fib))

    #for f in fib:    # sequenza infinita
    #    print(f)

    limited = list(islice(fib, 0, 10))  # numeri di Fibonacci da 11 a 20 (l'iterator 'ricorda' l'ultimo numero ritornato
    print(limited)


    def f(a, b):
        return a + b

    args = {'c': 1 ,'b': 2}

    print(f(**args))
    print(f(1,2))