from dictionary.dictTrees.binarySearchTree import BinarySearchTree
from dictionary.dictTrees.avlTree import AVLTree
from dictionary.linkedListDictionary import LinkedListDictionary

from hash.hashTable import *

from time import time

from pathlib import Path
import random


def dictionaryPerformance(ops, dic):
    start = time()
    for i in range(ops):
        dic.insert(i, i + 10)
    elapsed = time() - start
    print("Tempo totale per {} operazioni di INSERT: {} s".format(ops, elapsed))
    print("Tempo medio INSERT:", elapsed / ops, " s")

    start = time()
    for i in reversed(range(ops)):
        dic.search(i)
    elapsed = time() - start
    print("Tempo totale per {} operazioni di SEARCH: {} s".format(ops, elapsed))
    print("Tempo medio SEARCH:", elapsed / ops, " s")

    start = time()
    for i in range(ops):
        dic.delete(i)
    elapsed = time() - start
    print("Tempo totale per {} operazioni di DELETE: {} s".format(ops, elapsed))
    print("Tempo medio DELETE:", elapsed / ops, " s")




def dictionaryPerformanceSearch(ops, dic):

    start = time()
    for i in reversed(range(ops)):
        dic.search(i)
    elapsed = time() - start

    return elapsed


def dictionaryWriteResults(filename, dic):
    #funzione che crea un file csv con i tempi che il dizionario dic impiega nella ricerca
    #fate per casa i test per le operazioni di inserimento e cancellazione

    random.seed(12345)
    times = []
    ops = list( range(1000, 50000, 5000))

    for op in ops:
        print(op)
        for i in range(ops):
            dic.insert(i, i + 10)

        times.append(dictionaryPerformanceSearch(op, dic))

        for i in range(ops):  # restore dic
            dic.delete(i)

    #write results into a file
    path = filename + ".csv"
    file = Path(path)
    if not file.is_file():
        open(path, "w+")
    f = open(path, "a")

    for i in range(0, len(ops)):
        line = str(ops[i]) + "," + str(times[i]) + '\n'
        print(line)
        f.write(line)
    f.close()

def dictionaryTest():
    ll = LinkedListDictionary()
    print("LINKED LIST DICTIONARY")
    dictionaryWriteResults("list", ll)

    bst = BinarySearchTree()
    print("BINARY SEARCH TREE")
    dictionaryWriteResults("binaryTree", bst)

    avl = AVLTree()
    print("AVL TREE")
    dictionaryWriteResults("avl.csv", avl)

    m = 1000
    thl = TabellaHashListeColl(m)
    print("COLLISION LIST HASH TABLE")
    dictionaryWriteResults("hashTableColl", thl)

    m = 35000
    tha = TabellaHashAperta(m)
    print("OPEN ADDRESSING HASH TABLE")
    dictionaryWriteResults("hashTableOpen", tha)

def hashTest():

    m = 1000

    c1 = 0.4
    c2 = 0.6
    haq = HashingApertoScansioneQuadratica(m, HashingDivisione(m), c1, c2)
    thl = TabellaHashListeColl(m, haq)
    print("COLLISION LIST HASH TABLE - HASH QUADRATICO")
    dictionaryWriteResults("hashTableColl-quad", thl)

    hal = HashingApertoScansioneLineare(m)
    thl = TabellaHashListeColl(m, hal)
    print("COLLISION LIST HASH TABLE - HASH LINEARE")
    dictionaryWriteResults("hashTableColl-lin", thl)

    had = HashingApertoDoppio(m)
    thl = TabellaHashListeColl(m, had)
    print("COLLISION LIST HASH TABLE - HASH DOPPIO")
    dictionaryWriteResults("hashTableColl-doppio", thl)







if __name__ == "__main__":

    ops = 5000

    ll = LinkedListDictionary()
    print("LINKED LIST DICTIONARY")
    dictionaryPerformance(ops, ll)

    bst = BinarySearchTree()
    print("BINARY SEARCH TREE")
    dictionaryPerformance(ops, bst)

    avl = AVLTree()
    print("AVL TREE")
    dictionaryPerformance(ops, avl)

    m = 1000
    thl = TabellaHashListeColl(m)
    print("COLLISION LIST HASH TABLE")
    dictionaryPerformance(ops, thl)

    m = 5000
    tha = TabellaHashAperta(m)
    print("OPEN ADDRESSING HASH TABLE")
    dictionaryPerformance(ops, tha)

    dictionaryTest()
    hashTest()
