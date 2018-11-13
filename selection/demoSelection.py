"""
    File name: demoSelection.py
    Author: Giuseppe Chiapparo
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 20/10/2017
    Python Version: 3.5.2

    This module implements an example of usage of Selection module.
"""

import selection.Selection as Selection

import random
from random import randint
from time import time
import math

# Global parameters
amount = 10000
k = int(amount / 2)
position = math.ceil(amount / 2)
trivial = False


def test1():
    print("Input gia' ordinato. Lista di {} elementi.\n".format(amount))

    # ATT: in Python v. < 3 è sufficiente l = range(amount) perché range è una lista.
    #      in Python v. >= 3 range è un tipo di dato a parte da trasformare in lista.
    l = list(range(amount))
    start = time()
    res = Selection.sortSelect(l, position)
    elapsed = time() - start
    print("sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res))

    l = list(range(amount))
    start = time()
    res = Selection.heapSelect(l, position)
    elapsed = time() - start
    print("heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res))

    l = list(range(amount))
    start = time()
    res = Selection.quickSelectRand(l, position)
    elapsed = time() - start
    print("quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, position, res))

    l = list(range(amount))
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           position,
                                                                                                           res))

    l = list(range(amount))
    minLen = 15
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           position,
                                                                                                           res))

    l = list(range(amount))
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, position, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           position,
                                                                                                           res))

    if trivial:
        l = list(range(amount))
        start = time()
        res = Selection.trivialSelect(l, k)
        elapsed = time() - start
        print("trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    print("\nEnd.")


def test2():
    print("Input ordinato inversamente. Lista di {} elementi.\n".format(amount))

    l = list(range(amount, -1, -1))
    start = time()
    res = Selection.sortSelect(l, k)
    elapsed = time() - start
    print("sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(range(amount, -1, -1))
    start = time()
    res = Selection.heapSelect(l, k)
    elapsed = time() - start
    print("heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(range(amount, -1, -1))
    start = time()
    res = Selection.quickSelectRand(l, k)
    elapsed = time() - start
    print("quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(range(amount, -1, -1))
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    l = list(range(amount, -1, -1))
    minLen = 15
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    l = list(range(amount, -1, -1))
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    if trivial:
        l = list(range(amount, -1, -1))
        start = time()
        res = Selection.trivialSelect(l, k)
        elapsed = time() - start
        print("trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    print("\nEnd.")


def test3():
    print("Input random(0,{}). Lista di {} elementi.\n".format(amount, amount))

    basel = [randint(0, amount) for i in range(amount)]  # @UnusedVariable
    l = list(basel)
    start = time()
    res = Selection.sortSelect(l, k)
    elapsed = time() - start
    print("sortSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(basel)
    start = time()
    res = Selection.heapSelect(l, k)
    elapsed = time() - start
    print("heapSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(basel)
    start = time()
    res = Selection.quickSelectRand(l, k)
    elapsed = time() - start
    print("quickSelectRand takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    l = list(basel)
    minLen = 0
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    l = list(basel)
    minLen = 5
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    l = list(basel)
    minLen = 30
    start = time()
    res = Selection.quickSelectDet(l, k, minLen)
    elapsed = time() - start
    print("quickSelectDet (with minLen={}) takes {} seconds. Selected element in position {} is {}".format(minLen,
                                                                                                           elapsed,
                                                                                                           k,
                                                                                                           res))

    if trivial:
        l = list(basel)
        start = time()
        res = Selection.trivialSelect(l, k)
        elapsed = time() - start
        print("trivialSelect takes {} seconds. Selected element in position {} is {}".format(elapsed, k, res))

    print("\nEnd.")


def test4():
    print("Test con input size crescente. Input random(0,{}). Lista di {} elementi.\n".format(amount, amount))
    k = int(amount / 2)

    for i in range(50, 250, 5):
        random.seed(i)
        basel = [randint(0, (1 << 32) - 1) for j in range(1000*i)]  # @UnusedVariable
        l = list(basel)
        start = time()
        res = Selection.sortSelect(l, k)
        elapsed = time() - start
        print('{},{}'.format(1000*i, elapsed))


def test5():
    print("Test con k differenti. Input random(0,{}). Lista di {} elementi.\n".format(amount, amount))

    basel = [randint(0, 1 << 32) for i in range(amount)]  # @UnusedVariable
    k = int(amount / 2)

    kNumber = 101

    for i in range(1, kNumber):
        k = int(amount / kNumber) * i - 1
        l = list(basel)
        start = time()
        res = Selection.quickSelectDet(l, k, 10)
        elapsed = time() - start
        print('{},{}'.format(k, elapsed))


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
