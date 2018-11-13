"""
    File name: demoCode.py
    Author: Domenico Spera
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 15/10/2017
    Python Version: 3.5.2

    This module implements a usage example for Queue module.

"""

from datastruct.Queue import CodaListaCollegata
from datastruct.Queue import CodaArrayList
from datastruct.Queue import CodaArrayList_deque

from time import time


# global functions
def enqueueTest(q, n=50000):
    start = time()

    for i in range(n):
        q.enqueue(i)

    elapsed = time() - start

    print("Required time: ", elapsed, "seconds.")


def dequeueTest(q, n=50000):
    start = time()

    for i in range(n):  # @UnusedVariable
        q.dequeue()

    elapsed = time() - start

    print("Required time: ", elapsed, "seconds.")


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":

    print("\nEnqueueing elements...\n")

    print("CodaListaCollegata")
    ql = CodaListaCollegata()
    enqueueTest(ql)

    print("Coda - ArrayList")
    qal = CodaArrayList()
    enqueueTest(qal)

    print("Coda - ArrayList_deque")
    qald = CodaArrayList_deque()
    enqueueTest(qald)

    print("\nDequeueing elements\n")

    print("Coda - ListaCollegata")
    dequeueTest(ql)

    print("Coda - ArrayList")
    dequeueTest(qal)

    print("Coda - ArrayList_deque")
    dequeueTest(qald)
