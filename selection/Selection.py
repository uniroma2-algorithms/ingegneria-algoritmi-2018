"""
    File name: Selection.py
    Author: Giuseppe Chiapparo
    Date created: 11/10/2016
    Modified By: Laura Trivelloni
    Date last modified: 20/10/2017
    Python Version: 3.5.2

    This module implements the selection algorithms.
"""

from datastruct.HeapMin import HeapMin
from selection.__init__ import printSwitch
from math import ceil
from sorting.Sorting import mergeSort, partition

"""
    Selection of the k-th item in the list when k is small .
"""
def trivialSelect(l, k):

    if printSwitch.dumpOperations:
        print("trivialSelect of ", str(l), "with k", str(k))

    length = len(l)
    if k <= 0 or k > length:
        return None

    for i in range(0, k):
        minimum = i
        for j in range(i + 1, length):
            if l[j] < l[minimum]:
                minimum = j
        l[minimum], l[i] = l[i], l[minimum]

    if printSwitch.dumpOperations:
        print("   L'elemento nella posizione cercata: ", l[k - 1])
    return l[k - 1]


"""
    Sort the list and select of the k-th item in the list --> O(nlogn)
"""


def sortSelect(l, k):
    if printSwitch.dumpOperations:
        print("sortSelect")
    if k <= 0 or k > len(l):
        return None
    mergeSort(l)
    if printSwitch.dumpOperations:
        print(l)
    return l[k - 1]


"""
    Selection of the k-th item in the list when k is small.
"""


def heapSelect(l, k):
    if printSwitch.dumpOperations:
        print("heapSelect")
    if k <= 0 or k > len(l):
        return None

    heap = HeapMin(l)
    heap.heapify()
    if printSwitch.dumpOperations:
        print(heap.heap)

    for i in range(0, k - 1):  # @UnusedVariable i
        heap.deleteMin()

    if printSwitch.dumpOperations:
        print(heap.heap)

    return heap.findMin()


# BEGIN
""" 
    QUICKSELECT RANDOMIZZATO (ricorsivo)
    
    Prende un perno random x, ed individua gli elementi A <= x e quelli B > x.
    Se |A|+1=k, l'elemento cercato e' x. 
    Se |A|<=k, prosegue ricorsivamente la ricerca in A.
    Altrimenti prosegue ricorsivamente su B, cercando k'=k-(|A|+1)
    Richiede tempo atteso O(n)
    Somiglia a quickSort randomizzato, con la differenza che si fa una sola chiamata
    ricorsiva anziche' 2
"""


def quickSelectRand(l, k):  # k 1...n
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectRand(l, 0, len(l) - 1, k)


def recursiveQuickSelectRand(l, left, right, k):
    if printSwitch.dumpOperations:
        print("recursiveQuickSelectRand({},{},{})".format(left, right, k))

    if left > right:  # controllo superfluo
        return

    if left == right and k - 1 == left:
        return l[k - 1]

    mid = partition(l, left, right)
    if printSwitch.dumpOperations:
        print("mid: {}".format(mid))

    if k - 1 == mid:
        return l[mid]
    if k - 1 < mid:
        return recursiveQuickSelectRand(l, left, mid - 1, k)
    else:
        return recursiveQuickSelectRand(l, mid + 1, right, k)


# END


# BEGIN
""" 
    QUICKSELECT DETERMINISTICO
    Divide l'input in gruppi di 5 (tranne al piu' l'ultimo gruppo), e per ciascun
    gruppo calcola il mediano.
    Quindi calcola ricorsivamente il mediano dei mediani, ed utilizza quello come perno.
    Si puo' dimostrare che sia la sottosequenza sinistra che quella destra contengono
    al piu' 7n/10 elementi.
    Quindi il tempo d'esecuzione dell'algoritmo e' T(n)=O(n)+T(n/5)+T(7n/10)=O(n)
"""


def quickSelectDet(l, k, minLen, whoami="QuickSelectDet"):
    if k <= 0 or k > len(l):
        return None
    return recursiveQuickSelectDet(l, 0, len(l) - 1, k, minLen, whoami)


def recursiveQuickSelectDet(l, left, right, k, minLen, whoami):
    if printSwitch.dumpOperations:
        condOutput(whoami, "recursiveQuickSelectDet({},{},{},{})".format(left, right, k,
                                                                         minLen) + "\n" + "[" + "- " * left + str(
            l[left:right + 1])[1:-1] + "- " * (len(l) - right - 1) + "]")

    if left == right:
        return l[left]

    # si usa stop per decidere quando smettere di ricorrere ed utilizzare un algoritmo diverso
    if len(l) < minLen:
        med = trivialSelect(l[left: right + 1], k - left)
        if printSwitch.dumpOperations:
            condOutput(whoami, "return:" + str(med))
        return med

    # compute groups of five
    numElem = right - left + 1
    numGroups = int(ceil(numElem / 5.0))
    median = []
    for i in range(0, numGroups):
        dimGroup = 5 if (i < numGroups - 1 or numElem % 5 == 0) \
            else (numElem - (numGroups - 1) * 5)
        a = left + i * 5
        b = left + i * 5 + dimGroup - 1

        if printSwitch.dumpOperations:
            condOutput(whoami, "dimGroup: " + str(dimGroup) + "\n" + "Compute median in group {}".format(l[a:b + 1]))
        m = trivialSelect(l[a:b + 1], int(ceil(dimGroup / 2.0)))
        median.append(m)

    if printSwitch.dumpOperations:
        condOutput(whoami, "Compute the median of " + str(median))

    vperno = quickSelectDet(median, ceil(len(median) / 2), minLen, "Median Recursion on list {}".format(median))  #vperno è un valore e non un indice

    if printSwitch.dumpOperations:
        condOutput(whoami, "Partitioning wrt " + str(vperno))

    perno = partitionDet(l, left, right,
                         vperno)  # Watch: this is a new function which takes the pivot as the parameter

    posperno = perno + 1
    if posperno == k:
        if printSwitch.dumpOperations:
            condOutput(whoami, "return " + str(l[perno]))
        return l[perno]
    if posperno > k:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the LEFT partition.")
        return recursiveQuickSelectDet(l, left, perno - 1, k, minLen, whoami)
    else:
        if printSwitch.dumpOperations:
            condOutput(whoami, "Recursion on the RIGHT partition.")
        return recursiveQuickSelectDet(l, perno + 1, right, k, minLen, whoami)


def partitionDet(l, left, right, pivot):
    #nota: pivot è un valore dell'array l e non un indice!
    inf = left
    sup = right

    while True:
        while inf <= right and l[inf] <= pivot:
            if l[inf] == pivot and l[left] != pivot:
                l[left], l[inf] = l[inf], l[left]
            else:
                inf += 1

        while sup >= 0 and l[sup] > pivot:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[left], l[sup] = l[sup], l[left]

    # if printSwitch.dumpOperations:
    #    print("- "*left + str(l[left:right + 1]) + " -"*(len(l) - right - 1))

    return sup


# For debugging info
oldstate = ""


def condOutput(whoami, msg):
    global oldstate
    if oldstate != whoami:
        print("\t" + whoami)
        oldstate = whoami
    print(msg)


if __name__ == '__main__':
    basel = [5, 34, 26, 1, 4, 2, 17, 50, 41]
    k = 5
    l = list(basel)
    print(l)
    print(trivialSelect(l,k))
    # print(sortSelect(l, k))
    # print(heapSelect(l, k))
    # print(quickSelectRand(l, k))
    # print(quickSelectDet(l, k, 3))
    print(l)
