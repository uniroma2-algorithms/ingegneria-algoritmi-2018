"""
    File name: demoPile.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a usage example for Stack module.

"""

from datastruct.Stack import PilaListaCollegata
from datastruct.Stack import PilaArrayList_dummy
from datastruct.Stack import PilaArrayList

from time import time


# global functions

def pushTest(s, n=50000):

    start = time()

    for i in range(n):
        s.push(i)

    elapsed = time() - start

    print("Required time: ", elapsed, "seconds.")


def popTest(s, n=50000):

    start = time()

    for i in range(n):  # @UnusedVariable
        s.pop()

    elapsed = time() - start

    print("Required time: ", elapsed, "seconds.")


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":

    print("\nPushing elements...\n")

    print("Pila - Lista Collegata")
    sl = PilaListaCollegata()
    pushTest(sl)

    print("Pila - ArrayList_dummy")
    sald = PilaArrayList_dummy()
    pushTest(sald)

    print("Pila - ArrayList")
    sal = PilaArrayList()
    pushTest(sal)

    print("\nPopping elements...\n")

    print("Pila - Lista Collegata")
    popTest(sl)

    print("Pila - ArrayList_dummy")
    popTest(sald)

    print("Pila - ArrayList")
    popTest(sal)
